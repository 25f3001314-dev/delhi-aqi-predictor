# Render Deployment Guide - Delhi AQI Predictor

## 🚀 Quick Deploy on Render

### Step 1: Create Render Account
1. Go to: **https://render.com**
2. Sign up with GitHub (FREE)
3. Connect your GitHub account

### Step 2: Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your repository: `delhi-aqi-predictor`
3. Configure:
   - **Name**: `delhi-aqi-predictor`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`

### Step 3: Add Environment Variable
1. Go to **Environment** tab
2. Add:
   - **Key**: `AQI_API_KEY`
   - **Value**: `4e84e711ecd384cb72016b0238185ae0a443dbe3`
3. Click **Save Changes**

### Step 4: Deploy!
Click **"Create Web Service"** - Deployment will start automatically!

## 🌐 Your Live URL
After deployment (2-3 minutes):
```
https://delhi-aqi-predictor.onrender.com
```

## 📋 All Features Working:
- ✅ Real-time AQI Dashboard
- ✅ Live Location Tracking (auto-open)
- ✅ Sound Alerts (3 levels)
- ✅ ML-based Area Predictions
- ✅ AQI Map (10 Delhi areas)
- ✅ Hospital Finder (FREE OpenStreetMap)

## 🔄 Auto-Deploy
Any push to `main` branch = auto redeploy!

## 💰 Cost
**100% FREE** on Render free tier!

## 🐛 Troubleshooting
If build fails:
1. Check logs in Render dashboard
2. Verify `requirements.txt` has all dependencies
3. Ensure `gunicorn` is installed
