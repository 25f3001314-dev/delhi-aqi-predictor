# 🚀 Quick Setup Guide

## Live Location Alert Page

### Step 1: Get Free AQICN API Token
1. Visit [aqicn.org/api/register](https://aqicn.org/api/register)
2. Enter your email and click "Register"
3. You'll receive a token like: `abc123xyz456`
4. Open `live-location.html`
5. Find this line (around line 107):
   ```javascript
   const token = 'demo'; // Get your free token at aqicn.org/api/register
   ```
6. Replace `'demo'` with your token:
   ```javascript
   const token = 'abc123xyz456';
   ```
7. Save the file!

### Features:
- ✅ GPS auto-detect with fallback to IP location
- ✅ Works on mobile and desktop
- ✅ Browser notifications when AQI > 150
- ✅ Color-coded AQI categories
- ✅ Health advice based on pollution level

---

## Hospital Finder Page

### Step 1: Get Free Google Maps API Key
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project or select existing one
3. Enable these APIs:
   - **Places API** (for hospital search)
   - **Maps JavaScript API** (for map display)
4. Go to "Credentials" → "Create Credentials" → "API Key"
5. Copy your API key (looks like: `AIzaSyBxxx...`)

### Step 2: Add API Key to Code
1. Open `hospitals.html`
2. Scroll to the bottom (last few lines)
3. Find:
   ```html
   <script async defer
       src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_API_KEY&libraries=places&callback=initMap">
   </script>
   ```
4. Replace `YOUR_GOOGLE_API_KEY` with your actual key:
   ```html
   <script async defer
       src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBxxx...&libraries=places&callback=initMap">
   </script>
   ```
5. Save the file!

### Features:
- ✅ Finds hospitals within 5km
- ✅ Shows distance in kilometers
- ✅ Google Maps ratings
- ✅ One-click directions
- ✅ WhatsApp share location
- ✅ Interactive map with markers

---

## GitHub Pages Deployment

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Added live location and hospital finder pages"
git push origin main
```

### Step 2: Enable GitHub Pages
1. Go to your repo on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select branch: `main`
4. Click Save
5. Wait 2-3 minutes

### Step 3: Access Your Site
Your site will be live at:
```
https://YOUR_USERNAME.github.io/delhi-aqi-predictor/
```

**Page URLs:**
- Main page: `/` or `/index.html`
- Live alerts: `/live-location.html`
- Hospitals: `/hospitals.html`

---

## Testing Locally

### Option 1: Python HTTP Server
```bash
cd /workspaces/delhi-aqi-predictor
python -m http.server 8000
```
Then open: `http://localhost:8000`

### Option 2: VS Code Live Server
1. Install "Live Server" extension
2. Right-click on `public/index.html`
3. Select "Open with Live Server"

---

## Troubleshooting

### Live Location Not Working?
- ✅ Check if you replaced `'demo'` with your AQICN token
- ✅ Allow location permissions in browser
- ✅ Test on HTTPS (GitHub Pages uses HTTPS automatically)

### Hospital Map Not Loading?
- ✅ Check if you added your Google Maps API key
- ✅ Verify Places API and Maps JavaScript API are enabled
- ✅ Check browser console for errors (F12)

### Mobile Issues?
- ✅ Both pages are mobile-responsive
- ✅ Location works better on mobile (GPS available)
- ✅ Allow browser permissions when prompted

---

## Free API Limits

| Service | Free Limit | Cost After |
|---------|-----------|------------|
| AQICN | 1,000 requests/day | Free forever |
| Google Maps | $200 credit/month (~28,000 loads) | Pay as you go |

**Note:** For personal/demo use, you'll never hit these limits! 🎉

---

## Next Steps

1. ✅ Get both API keys (takes 5 minutes)
2. ✅ Update the code with your keys
3. ✅ Test locally to ensure everything works
4. ✅ Push to GitHub and enable Pages
5. ✅ Share your live site with friends! 🚀

Need help? Check the browser console (F12) for error messages.
