import requests
import os
from datetime import datetime
from flask import Flask, render_template, jsonify, request
from aqi_model import predict_aqi_for_location, get_all_areas_prediction

app = Flask(__name__)

# Configuration
AQI_API_KEY = os.getenv("AQI_API_KEY", "4e84e711ecd384cb72016b0238185ae0a443dbe3")
AQI_API_URL = "https://api.waqi.info/feed/delhi/"

def get_real_time_aqi(city="delhi"):
    """Fetch real-time AQI from WAQI API"""
    try:
        response = requests.get(f"https://api.waqi.info/feed/{city}/?token={AQI_API_KEY}", timeout=5)
        data = response.json()
        
        if data.get("status") == "ok":
            aqi_data = data["data"]
            return {
                "aqi": aqi_data.get("aqi", 0),
                "city": aqi_data.get("city", {}).get("name", city),
                "time": aqi_data.get("time", {}).get("s", ""),
                "pm25": aqi_data.get("iaqi", {}).get("pm25", {}).get("v", 0),
                "pm10": aqi_data.get("iaqi", {}).get("pm10", {}).get("v", 0),
                "temp": aqi_data.get("iaqi", {}).get("t", {}).get("v", 0),
                "humidity": aqi_data.get("iaqi", {}).get("h", {}).get("v", 0),
                "source": "real-time"
            }
    except Exception as e:
        print(f"API Error: {e}")
    
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-location')
def live_location():
    return render_template('live-location.html')

@app.route('/hospitals')
def hospitals():
    return render_template('hospitals.html')

@app.route('/aqi-map')
def aqi_map():
    return render_template('aqi-map.html')

@app.route('/api/predict-aqi', methods=['POST'])
def predict_aqi():
    """API endpoint for ML-based AQI prediction combined with real-time data"""
    data = request.json
    lat = data.get('lat')
    lng = data.get('lng')
    
    if not lat or not lng:
        return jsonify({"error": "Latitude and longitude required"}), 400
    
    # Get ML prediction
    ml_prediction = predict_aqi_for_location(float(lat), float(lng))
    
    # Try to get real-time data
    real_time_data = get_real_time_aqi()
    
    if real_time_data:
        # Combine ML prediction with real-time data (weighted average)
        combined_aqi = int((ml_prediction["aqi"] * 0.4) + (real_time_data["aqi"] * 0.6))
        ml_prediction["aqi"] = combined_aqi
        ml_prediction["real_time_aqi"] = real_time_data["aqi"]
        ml_prediction["ml_aqi"] = ml_prediction["aqi"]
        ml_prediction["pm25"] = real_time_data["pm25"]
        ml_prediction["pm10"] = real_time_data["pm10"]
        ml_prediction["source"] = "hybrid"
    
    return jsonify(ml_prediction)

@app.route('/api/all-areas')
def all_areas():
    """Get predictions for all Delhi areas with real-time adjustment"""
    predictions = get_all_areas_prediction()
    
    # Get real-time data for calibration
    real_time_data = get_real_time_aqi()
    
    if real_time_data:
        # Adjust all predictions based on real-time data
        adjustment_factor = real_time_data["aqi"] / 180  # 180 is baseline
        for pred in predictions:
            pred["aqi"] = int(pred["aqi"] * adjustment_factor)
            pred["source"] = "calibrated"
    
    return jsonify(predictions)

@app.route('/api/real-time')
def real_time_api():
    """Direct real-time AQI data endpoint"""
    data = get_real_time_aqi()
    if data:
        return jsonify(data)
    return jsonify({"error": "Unable to fetch real-time data"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=7860)
