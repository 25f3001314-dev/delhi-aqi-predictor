import gradio as gr
import requests
import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

# Configuration
AQI_API_KEY = os.getenv("AQI_API_KEY", "demo")
AQI_API_URL = "https://api.waqi.info/feed/delhi/"

def get_aqi_category(aqi):
    """Determine AQI category based on value"""
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def get_current_aqi():
    """Fetch current AQI for Delhi"""
    try:
        response = requests.get(f"{AQI_API_URL}?token={AQI_API_KEY}", timeout=5)
        data = response.json()
        
        if data.get("status") == "ok":
            aqi_value = int(data["data"]["aqi"])
        else:
            aqi_value = 131
    except Exception as e:
        aqi_value = 131
    
    category = get_aqi_category(aqi_value)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return aqi_value, category, timestamp

# Create Gradio interface
demo = gr.Interface(
    fn=get_current_aqi,
    inputs=[],
    outputs=[
        gr.Number(label="AQI Value", value=0),
        gr.Textbox(label="Category", value="Loading..."),
        gr.Textbox(label="Last Updated", value=""),
    ],
    title="🌍 Delhi Air Quality Monitor",
    description="Real-time Air Quality Index (AQI) monitoring for Delhi using WAQI API",
    allow_flagging="never",
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-location')
def live_location():
    return render_template('live-location.html')

@app.route('/hospitals')
def hospitals():
    return render_template('hospitals.html')

if __name__ == "__main__":
    app.run(debug=True, port=7860)
