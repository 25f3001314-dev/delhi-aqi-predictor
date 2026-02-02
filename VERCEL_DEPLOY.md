# 🚀 Vercel Deployment Guide - Delhi AQI Predictor

## ✅ Quick Deployment (3 Steps)

### Option 1: Vercel CLI (Fastest)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   cd /workspaces/delhi-aqi-predictor
   vercel --prod
   ```

### Option 2: GitHub Integration (Recommended)

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository: `25f3001314-dev/delhi-aqi-predictor`
4. Vercel will auto-detect settings
5. Click "Deploy"

**That's it!** Your app will be live at: `https://delhi-aqi-predictor.vercel.app`

## 🎯 Configuration Already Done

✅ `vercel.json` - Configured for serverless deployment
✅ `api/index.py` - Flask app wrapper for Vercel
✅ Environment variables - API key included
✅ Routes - All routes mapped correctly

## 🆓 Free Tier Benefits

- ✅ Unlimited deployments
- ✅ 100 GB bandwidth/month
- ✅ Auto HTTPS/SSL
- ✅ Fast global CDN
- ✅ Auto preview deployments for each commit
- ✅ No cold start issues

## 📊 Deployment Info

- **Build Time:** 30-60 seconds
- **Function Region:** Auto (closest to user)
- **Python Runtime:** 3.9+
- **Framework:** Flask (serverless)

## 🔄 Auto-Deploy

Once connected to GitHub, Vercel will automatically deploy:
- ✅ Every push to `main` branch
- ✅ Preview for every pull request
- ✅ Instant rollback if needed

## 🌐 Your URLs

After deployment:
- **Production:** `https://delhi-aqi-predictor.vercel.app`
- **Dashboard:** `https://vercel.com/dashboard`

## ⚙️ Environment Variables

Already configured in `vercel.json`:
```json
{
  "AQI_API_KEY": "4e84e711ecd384cb72016b0238185ae0a443dbe3"
}
```

To change later:
1. Go to Vercel Dashboard
2. Project Settings > Environment Variables
3. Update `AQI_API_KEY`

## 📝 Notes

- Vercel uses serverless functions (faster than Render!)
- No server management needed
- Automatic scaling based on traffic
- Better performance than Render free tier
