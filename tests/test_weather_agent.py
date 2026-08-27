"""
Automated Test Suite for Versha: Weather & Environmental AI Agent
Includes tests for Umbrella Advisories, Outdoor Fitness Scoring, and City Comparison.
Run: python -m unittest discover -s tests -p "test_*.py" -v
"""

import unittest
from src.tools import (
    fetch_weather_data,
    format_weather_report,
    calculate_outdoor_score,
    format_city_comparison
)
from src.agent import WeatherAIAgent


class TestVershaWeatherAIAgent(unittest.TestCase):
    def setUp(self):
        self.agent = WeatherAIAgent()

    def test_01_fetch_weather_bengaluru(self):
        data = fetch_weather_data("Bengaluru")
        self.assertIn("city", data)
        self.assertIn("temp_C", data)
        self.assertIn("humidity", data)
        self.assertIn("weather_desc", data)
        self.assertIn("rain_chance_percent", data)
        self.assertIn("umbrella_advisory", data)
        self.assertIn("outdoor_fitness_score", data)

    def test_02_umbrella_advisory_detection(self):
        data = fetch_weather_data("Mumbai")
        self.assertIn("umbrella_required", data)
        self.assertIsInstance(data["umbrella_required"], bool)

    def test_03_outdoor_fitness_scoring_algorithm(self):
        # Test ideal conditions
        ideal_score, ideal_rating = calculate_outdoor_score(22.0, 50.0, 0.0, 3.0, 10.0)
        self.assertGreaterEqual(ideal_score, 8.0)
        self.assertIn("Excellent", ideal_rating)

        # Test extreme heat & rain conditions
        harsh_score, harsh_rating = calculate_outdoor_score(42.0, 90.0, 80.0, 9.0, 40.0)
        self.assertLessEqual(harsh_score, 4.0)

    def test_04_city_extraction_single_and_multi(self):
        # Single city
        self.assertEqual(self.agent.extract_cities("What is the weather in Pune?"), ["Pune"])
        self.assertEqual(self.agent.extract_cities("Weather for Hyderabad"), ["Hyderabad"])
        
        # Multi-city comparison
        comp_cities = self.agent.extract_cities("Compare weather between Bengaluru and Delhi")
        self.assertEqual(comp_cities, ["Bengaluru", "Delhi"])

    def test_05_multi_city_comparison_pipeline(self):
        res = self.agent.execute("Compare weather between Bengaluru and Delhi")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["mode"], "comparison")
        self.assertIn("Bengaluru", res["telemetry"])
        self.assertIn("Delhi", res["telemetry"])
        self.assertIn("Location Comparison", res["response"])

    def test_06_versha_execution_pipeline_and_persona(self):
        res = self.agent.execute("What is the weather in Bengaluru?")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["agent"], "Versha")
        self.assertEqual(res["detected_city"], "Bengaluru")
        self.assertIn("telemetry", res)
        self.assertIn("response", res)
        self.assertIn("Hello!", res["response"])

    def test_07_invalid_city_graceful_handling(self):
        res = self.agent.execute("Weather in NonExistentCityXYZ123")
        self.assertIn("telemetry", res)
        self.assertEqual(res["status"], "success")


if __name__ == "__main__":
    unittest.main()
