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
    """Fetch real-time AQI from WAQI API with all available data"""
    try:
        response = requests.get(f"https://api.waqi.info/feed/{city}/?token={AQI_API_KEY}", timeout=5)
        data = response.json()
        
        if data.get("status") == "ok":
            aqi_data = data["data"]
            iaqi = aqi_data.get("iaqi", {})
            
            # Extract all available parameters
            result = {
                "aqi": aqi_data.get("aqi", 0),
                "city": aqi_data.get("city", {}).get("name", city),
                "time": aqi_data.get("time", {}).get("s", ""),
                "pm25": iaqi.get("pm25", {}).get("v", 0),
                "pm10": iaqi.get("pm10", {}).get("v", 0),
                "temp": iaqi.get("t", {}).get("v", 0),
                "humidity": iaqi.get("h", {}).get("v", 0),
                "pressure": iaqi.get("p", {}).get("v", 0),
                "wind": iaqi.get("w", {}).get("v", 0),
                "dew": iaqi.get("dew", {}).get("v", 0),
                "o3": iaqi.get("o3", {}).get("v", 0),
                "no2": iaqi.get("no2", {}).get("v", 0),
                "so2": iaqi.get("so2", {}).get("v", 0),
                "co": iaqi.get("co", {}).get("v", 0),
                "uv": aqi_data.get("forecast", {}).get("daily", {}).get("uvi", [{}])[0].get("avg", 0) if aqi_data.get("forecast") else 0,
                "source": "real-time"
            }
            
            # Get attribution and station info
            if "attributions" in aqi_data:
                result["station"] = aqi_data.get("attributions", [{}])[0].get("name", "")
            
            return result
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

@app.route('/api/historical')
def historical_api():
    """Simulated historical data for chart (last 24 hours)"""
    import random
    from datetime import datetime, timedelta
    
    historical_data = []
    base_time = datetime.now()
    
    # Get current real AQI as baseline
    real_data = get_real_time_aqi()
    base_aqi = real_data["aqi"] if real_data else 180
    
    # Generate 24 hours of data (hourly)
    for i in range(24):
        time = base_time - timedelta(hours=23-i)
        # Vary AQI realistically around base value
        variation = random.randint(-30, 30)
        aqi = max(50, min(350, base_aqi + variation))
        
        historical_data.append({
            "timestamp": time.strftime("%H:%M"),
            "aqi": aqi
        })
    
    return jsonify(historical_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
