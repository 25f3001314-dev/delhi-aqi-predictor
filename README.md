---
title: Delhi Air Quality Predictor
emoji: 🌍
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.1"
python_version: "3.10"
app_file: app.py
pinned: false
---

# Delhi Air Quality Predictor

Real-time Air Quality Index monitoring for Delhi with location-based alerts and hospital finder.

## Features

- 🏠 **Main Page**: Live AQI data from WAQI API with real-time updates
- 📍 **Live Location Alert** (`live-location.html`): Get AQI for your current location with pollution notifications
- 🏥 **Hospital Finder** (`hospitals.html`): Find nearest hospitals with distance and Google Maps integration

## Pages

### 1. Main Page (index.html)
Real-time AQI monitoring dashboard with historical data

### 2. Live Location Alert (live-location.html)
- Auto-detects your location using GPS or IP fallback
- Shows current AQI at your location
- Browser notifications for high pollution levels (AQI > 150)
- **Setup**: Get free API token from [aqicn.org/api/register](https://aqicn.org/api/register) and replace `demo` in the code

### 3. Nearest Hospitals (hospitals.html)
- Finds hospitals within 5km radius
- Shows distance, ratings, and addresses
- Google Maps integration for directions
- Share location via WhatsApp
- **Setup**: Get free Google Maps API key from [console.cloud.google.com](https://console.cloud.google.com)
  - Enable "Places API" and "Maps JavaScript API"
  - Replace `YOUR_GOOGLE_API_KEY` in the code

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:7860`

## GitHub Pages Setup

1. Push these files to GitHub
2. Go to Settings → Pages
3. Select branch `main` and root directory
4. Your site will be live at `https://yourusername.github.io/delhi-aqi-predictor`
5. Update API keys in:
   - `live-location.html` → AQICN token
   - `hospitals.html` → Google Maps API key

## API Keys Required

| Page | API | Free Signup |
|------|-----|-------------|
| Live Location Alert | AQICN | [aqicn.org/api/register](https://aqicn.org/api/register) |
| Hospital Finder | Google Maps | [console.cloud.google.com](https://console.cloud.google.com) |

