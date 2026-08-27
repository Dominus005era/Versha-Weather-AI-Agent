"""
Versha: Weather & Environmental AI Agent - Interactive CLI Interface
Persona: Versha (Intelligent Weather & Environmental AI Assistant)
Features: Live Telemetry, Rain/Umbrella Alerts, Outdoor Fitness Score, Multi-City Comparison
Workshop: AWS AI Webinar by Skill Nebula
Run: python main.py
"""

import sys
import json

# Ensure UTF-8 console encoding in Windows PowerShell and Command Prompt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from src.agent import WeatherAIAgent

BANNER = """
========================================================================
[+] VERSHA: REAL-TIME WEATHER & ENVIRONMENTAL AI AGENT
    Persona   : Versha (Intelligent Weather & Environmental Assistant)
    Features  : Live Telemetry | Rain Advisory | Outdoor Score | Comparison
    Framework : Strands Agents + Ollama Architecture
    APIs      : wttr.in & AQI Open Environmental Endpoints
========================================================================
"""


def print_result(res: dict):
    print("\n" + "-"*65)
    print(f"[*] [AI Agent]         : {res['agent']}")
    if res.get("mode") == "comparison":
        cities_str = " vs ".join([c.upper() for c in res.get("detected_cities", [])])
        print(f"[*] [Comparison Mode]  : {cities_str}")
    else:
        print(f"[*] [Target Location]  : {res.get('detected_city', 'UNKNOWN').upper()}")
    print(f"[*] [Execution Status] : {res['status'].upper()}")
    print(f"[*] [Architecture]     : {res['framework']}")
    print("-" * 65)
    print(f"[>] [Versha's Response]:\n{res['response']}\n")
    
    print("[#] [Live Telemetry JSON Payload]:")
    print(json.dumps(res['telemetry'], indent=2))
    print("=" * 65 + "\n")


def main():
    print(BANNER)
    agent = WeatherAIAgent()

    print("Versha: Hello! I am Versha, your real-time Weather and Environmental AI Assistant.")
    print("        I can help you monitor live weather, umbrella alerts, outdoor fitness scores,")
    print("        and compare conditions between multiple cities.\n")

    print("[?] Sample Queries to Demonstrate:")
    print("   1. 'What is the current weather in Bengaluru?' (Live Telemetry + Umbrella Alert)")
    print("   2. 'Should I carry an umbrella in Mumbai today?' (Rain Advisory)")
    print("   3. 'Outdoor fitness score for Delhi' (Running/Cycling Feasibility Index)")
    print("   4. 'Compare weather between Bengaluru and Delhi' (Side-by-Side Comparison)")
    print("   5. 'Check weather in London'")
    print("   6. Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("User > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Versha: Goodbye! Have a wonderful and safe day ahead!")
                break

            result = agent.execute(user_input)
            print_result(result)

        except KeyboardInterrupt:
            print("\nVersha: Session ended. Goodbye!")
            break
        except Exception as e:
            print(f"[Error]: {e}")


if __name__ == "__main__":
    main()
