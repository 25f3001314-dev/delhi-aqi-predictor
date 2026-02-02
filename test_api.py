import requests
import json

print("="*60)
print("TESTING LIVE API - DELHI AQI")
print("="*60)

try:
    response = requests.get(
        'https://api.waqi.info/feed/delhi/?token=4e84e711ecd384cb72016b0238185ae0a443dbe3',
        timeout=10
    )
    data = response.json()
    
    print(f"\n✅ API Status: {data.get('status')}")
    
    if data.get('status') == 'ok':
        aqi_data = data['data']
        iaqi = aqi_data.get('iaqi', {})
        
        print("\n" + "="*60)
        print("LIVE DATA FROM WAQI API:")
        print("="*60)
        print(f"\n🔴 AQI: {aqi_data.get('aqi')} (US Standard)")
        print(f"📍 Location: {aqi_data.get('city', {}).get('name')}")
        print(f"🕒 Last Update: {aqi_data.get('time', {}).get('s')}")
        
        print("\n--- POLLUTANTS ---")
        print(f"PM2.5: {iaqi.get('pm25', {}).get('v', 'N/A')} µg/m³")
        print(f"PM10: {iaqi.get('pm10', {}).get('v', 'N/A')} µg/m³")
        print(f"O3 (Ozone): {iaqi.get('o3', {}).get('v', 'N/A')}")
        print(f"NO2: {iaqi.get('no2', {}).get('v', 'N/A')}")
        print(f"SO2: {iaqi.get('so2', {}).get('v', 'N/A')}")
        print(f"CO: {iaqi.get('co', {}).get('v', 'N/A')}")
        
        print("\n--- WEATHER CONDITIONS ---")
        print(f"🌡️ Temperature: {iaqi.get('t', {}).get('v', 'N/A')}°C")
        print(f"💧 Humidity: {iaqi.get('h', {}).get('v', 'N/A')}%")
        print(f"📊 Pressure: {iaqi.get('p', {}).get('v', 'N/A')} mb")
        print(f"💨 Wind: {iaqi.get('w', {}).get('v', 'N/A')} km/h")
        print(f"💦 Dew Point: {iaqi.get('dew', {}).get('v', 'N/A')}°C")
        
        print("\n" + "="*60)
        print("✅ CONFIRMATION: ALL DATA IS 100% LIVE FROM INTERNET")
        print("="*60)
        print(f"\n📡 Data Source: {aqi_data.get('attributions', [{}])[0].get('name', 'WAQI')}")
        print(f"🔗 API Endpoint: https://api.waqi.info/feed/delhi/")
        
    else:
        print(f"\n❌ API Error: {data}")
        
except Exception as e:
    print(f"\n❌ Connection Error: {e}")
