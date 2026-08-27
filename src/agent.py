"""
Versha: Weather & Environmental AI Agent Engine
Persona: Versha (Intelligent Weather, Climate & Environmental Assistant)
Architecture: Strands Agents Framework + Ollama Compatible + HTTP Tools
Includes Smart Umbrella Alerts, Outdoor Fitness Scoring, and Multi-City Comparison.
"""

import os
import sys
import re
from typing import Dict, Any, List
from src.tools import fetch_weather_data, format_weather_report, format_city_comparison

SYSTEM_PROMPT = """
You are Versha, an intelligent and friendly Weather & Environmental AI Assistant.
Your primary role is to assist users by providing real-time weather metrics, AQI, humidity,
wind speed, solar cycles (sunrise/sunset), rain/umbrella advisories, outdoor activity feasibility scores,
and multi-city comparisons.
You use the http_request tool and open API endpoints (wttr.in and WAQI) to fetch live data.
Always deliver accurate, structured environmental insights.
For weather data use: https://wttr.in/<city>?format=j1
For AQI use: https://api.waqi.info/feed/<city>/?token=demo
"""


class WeatherAIAgent:
    """
    Versha AI Agent supporting both Strands + Ollama integration
    and native high-speed tool execution.
    """
    def __init__(self, agent_name: str = "Versha", model_id: str = "gemma4:31b-cloud", host: str = "http://127.0.0.1:11434"):
        self.agent_name = agent_name
        self.user_name = "User"
        self.model_id = model_id
        self.host = host
        self.system_prompt = SYSTEM_PROMPT.strip()
        self.strands_available = False
        self.strands_agent = None

        # Attempt initializing Strands framework if installed and Ollama is active
        try:
            from strands import Agent
            from strands.models.ollama import OllamaModel
            
            model = OllamaModel(host=self.host, model_id=self.model_id)
            self.strands_agent = Agent(
                model=model,
                tools=[fetch_weather_data],
                system_prompt=self.system_prompt
            )
            self.strands_available = True
        except Exception:
            self.strands_available = False

    def extract_cities(self, prompt: str) -> List[str]:
        """
        Extracts one or multiple city names from the user query.
        Handles comparison formats:
        - "Compare weather between Bengaluru and Delhi"
        - "Bengaluru vs Mumbai"
        - "Compare London and Paris"
        """
        p = prompt.strip().rstrip("?.! ")
        lower_p = p.lower()

        # Check for comparison patterns
        m = re.search(r'\bbetween\s+([a-zA-Z\s]+?)\s+and\s+([a-zA-Z\s]+)', p, re.IGNORECASE)
        if m:
            return [m.group(1).strip(), m.group(2).strip()]

        m = re.search(r'\b([a-zA-Z]+)\s+(?:vs|versus)\s+([a-zA-Z]+)', p, re.IGNORECASE)
        if m:
            return [m.group(1).strip(), m.group(2).strip()]

        m = re.search(r'\bcompare\s+([a-zA-Z]+)\s+and\s+([a-zA-Z]+)', p, re.IGNORECASE)
        if m:
            return [m.group(1).strip(), m.group(2).strip()]

        # Single city extraction
        for kw in [" in ", " for ", " at ", " of "]:
            if kw in lower_p:
                parts = p.split(kw if kw in p else kw.title())
                if len(parts) > 1:
                    city_candidate = parts[-1].strip("?.! ")
                    return [city_candidate.split()[0] if " " in city_candidate else city_candidate]

        words = p.split()
        if len(words) == 1 and words[0].isalpha():
            return [words[0]]

        return ["Bengaluru"]

    def execute(self, user_prompt: str) -> Dict[str, Any]:
        """
        Executes user query, routes to the weather API tool, and formats Versha's response.
        Supports single-location reports and multi-city comparative analysis.
        """
        cities = self.extract_cities(user_prompt)

        # Multi-City Comparison Mode
        if len(cities) >= 2:
            city1, city2 = cities[0], cities[1]
            telemetry1 = fetch_weather_data(city1)
            telemetry2 = fetch_weather_data(city2)
            comparison_text = format_city_comparison(telemetry1, telemetry2)

            versha_response = f"Hello! Here is the comparative atmospheric analysis between {city1.title()} and {city2.title()}:\n\n{comparison_text}"

            return {
                "agent": self.agent_name,
                "mode": "comparison",
                "framework": "Strands-Agents Architecture (Ollama Ready)",
                "user_prompt": user_prompt,
                "detected_cities": [city1, city2],
                "status": "success",
                "telemetry": {
                    city1: telemetry1,
                    city2: telemetry2
                },
                "response": versha_response
            }

        # Single City Diagnostics Mode
        city = cities[0]
        raw_telemetry = fetch_weather_data(city)
        formatted_summary = format_weather_report(raw_telemetry)

        versha_response = f"Hello! Here is the latest atmospheric update and environmental advisory I retrieved for you:\n\n{formatted_summary}"

        return {
            "agent": self.agent_name,
            "mode": "single_city",
            "framework": "Strands-Agents Architecture (Ollama Ready)",
            "user_prompt": user_prompt,
            "detected_city": city,
            "status": "success",
            "telemetry": raw_telemetry,
            "response": versha_response
        }
