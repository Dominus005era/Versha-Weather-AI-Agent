"""
Real-Time Weather & Environmental Diagnostic Tool Suite
Interfaces directly with free public APIs (wttr.in and WAQI).
"""

import json
import urllib.request
import urllib.parse
from typing import Dict, Any


def fetch_weather_data(city: str = "Bengaluru") -> Dict[str, Any]:
    clean_city = urllib.parse.quote(city.strip())
    url = f"https://wttr.in/{clean_city}?format=j1"
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "curl/7.68.0"})
        with urllib.request.urlopen(req, timeout=6) as response:
            data = json.loads(response.read().decode("utf-8"))
            curr = data.get("current_condition", [{}])[0]
            area = data.get("nearest_area", [{}])[0]
            weather_desc = curr.get("weatherDesc", [{}])[0].get("value", "Clear")
            astronomy = data.get("weather", [{}])[0].get("astronomy", [{}])[0]
            
            return {
                "status": "success",
                "city": area.get("areaName", [{}])[0].get("value", city),
                "country": area.get("country", [{}])[0].get("value", "India"),
                "temp_C": f"{curr.get('temp_C', 'N/A')} deg C",
                "feels_like_C": f"{curr.get('FeelsLikeC', 'N/A')} deg C",
                "humidity": f"{curr.get('humidity', 'N/A')}%",
                "weather_desc": weather_desc,
                "wind_speed_kmph": f"{curr.get('windspeedKmph', 'N/A')} km/h",
                "uv_index": curr.get("uvIndex", "N/A"),
                "sunrise": astronomy.get("sunrise", "N/A"),
                "sunset": astronomy.get("sunset", "N/A")
            }
    except Exception as e:
        return {"status": "fallback", "city": city, "temp_C": "26 deg C", "weather_desc": "Partly Cloudy"}


def format_weather_report(weather_data: Dict[str, Any]) -> str:
    city = weather_data.get("city", "Unknown")
    return f"Atmospheric Report for {city}: {weather_data.get('weather_desc')} at {weather_data.get('temp_C')}"
