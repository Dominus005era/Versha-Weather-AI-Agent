"""
Versha: Weather & Environmental AI Agent Engine
"""
import os
import sys
from typing import Dict, Any
from src.tools import fetch_weather_data, format_weather_report

SYSTEM_PROMPT = """
You are Versha, an intelligent and friendly Weather & Environmental AI Assistant.
For weather data use: https://wttr.in/<city>?format=j1
"""

class WeatherAIAgent:
    def __init__(self, agent_name: str = "Versha"):
        self.agent_name = agent_name
        self.user_name = "User"

    def extract_city(self, prompt: str) -> str:
        words = prompt.strip().split()
        return words[-1].strip("?.! ") if words else "Bengaluru"

    def execute(self, user_prompt: str) -> Dict[str, Any]:
        city = self.extract_city(user_prompt)
        raw_telemetry = fetch_weather_data(city)
        formatted = format_weather_report(raw_telemetry)
        return {"agent": self.agent_name, "status": "success", "telemetry": raw_telemetry, "response": formatted}
