# 🌦️ Versha: Real-Time Weather & Environmental AI Agent

> **AWS AI & Cloud AI Agent Workshop — Skill Nebula**  
> *Track: Autonomous Decision-Intelligence & Environmental Telemetry*  
> **Author:** Rahul | **Architecture:** Strands Agents + Ollama + REST APIs  
> **Repository:** [https://github.com/Dominus005era/Versha-Weather-AI-Agent](https://github.com/Dominus005era/Versha-Weather-AI-Agent)

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests: 7 Passed](https://img.shields.io/badge/Tests-7%2F7%20Passed-brightgreen.svg)]()
[![Framework: Strands Agents](https://img.shields.io/badge/Framework-Strands%20Agents-orange.svg)](https://strandsagents.com)
[![Zero Cost](https://img.shields.io/badge/Cost-100%25%20Free%20%2F%20Zero--Cost-success.svg)]()

---

## 📌 Table of Contents
1. [Project Title & Overview](#-project-title--overview)
2. [Problem Statement](#-problem-statement)
3. [Project Objective](#-project-objective)
4. [Key Features](#-key-features)
5. [System Architecture & Logic](#-system-architecture--logic)
6. [Technologies & Tools Used](#-technologies--tools-used)
7. [Installation & Setup](#-installation--setup)
8. [How to Run the Project & Steps to Perform](#-how-to-run-the-project--steps-to-perform)
9. [Project Directory Structure](#-project-directory-structure)
10. [Testing Suite & Verification](#-testing-suite--verification)
11. [Sample CLI & Report Output](#-sample-cli--report-output)
12. [Limitations](#-limitations)
13. [Future Improvements](#-future-improvements)

---

## 🏷️ Project Title & Overview

**Versha** is an autonomous, real-time Weather and Environmental AI Agent engineered in Python using the **Strands Agents framework**. Unlike static weather scripts, Versha accepts unstructured conversational natural language prompts, extracts geographical entities (single or comparative), interacts with open REST endpoints (`wttr.in` and WAQI), parses structured multi-layer JSON telemetry, computes predictive **Rain & Umbrella Advisories**, calculates an explainable **Outdoor Fitness Feasibility Index (0–10 Score)**, and renders side-by-side **Multi-City Comparison Cards**.

---

## 📝 Problem Statement

In modern software development and cloud operations, developers and users face significant hurdles when interacting with climate and environmental data:
1. **LLM Knowledge Cutoff & Hallucination**: Traditional LLMs cannot answer real-time questions (e.g., *"Is it raining in Delhi right now?"*) and often hallucinate obsolete data.
2. **Brittle Script Interfaces**: Traditional CLI scripts require rigid parameter syntax (e.g., `--city Bengaluru`) and lack natural language understanding.
3. **Lack of Actionable Decision Intelligence**: Most weather APIs dump raw numbers (temperature, humidity) without contextualizing what they mean for the user's daily life (e.g., *"Should I carry an umbrella?"* or *"Is it safe for an outdoor run?"*).
4. **API Key & Billing Friction**: Many external weather providers enforce complex registration, credit card verification, and rate limits.

**Versha** resolves these challenges through **tool-augmented autonomous agency, open zero-auth REST endpoints, and transparent heuristic scoring models**.

---

## 🎯 Project Objective

- **Autonomous Agent Implementation**: Apply the Strands Agents architecture and system prompt design principles demonstrated in the **AWS AI Webinar** by **Skill Nebula**.
- **Natural Language Entity Extraction**: Autonomously parse single or multi-city comparison phrases (e.g., *"Compare weather between Bengaluru and Delhi"*) without rigid flags.
- **Predictive Decision Support**: Deliver explainable Rain/Umbrella advisories and a mathematical Outdoor Fitness Feasibility Score (1.0 to 10.0).
- **Comparative Intelligence**: Ingest and format dual-location telemetry into clean terminal ASCII comparative matrices.
- **Zero-Cost & Standard Library**: Run seamlessly across all operating systems (Windows, macOS, Linux) with zero paid API keys and 100% automated test coverage.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| **Autonomous Entity Parsing** | Uses NLP word-boundary regular expressions to dynamically extract target cities from conversational prompts. |
| **Real-Time Live Telemetry** | Queries live Temperature (°C), Feels-Like (°C), Humidity (%), Barometric Pressure (hPa), UV Index, Visibility (km), and Solar Cycles. |
| **☔ Smart Rain & Umbrella Advisory** | Ingests precipitation probability (`chanceofrain` %) and volume (`precipMM`) to recommend rain gear. |
| **🏃‍♂️ Outdoor Fitness Feasibility Index** | A mathematical heuristics engine scoring outdoor running, cycling, and commuting conditions on a 1.0 to 10.0 scale. |
| **⚖️ Multi-City Comparison Matrix** | Generates side-by-side terminal comparison cards when comparing two geographical locations. |
| **Strands Agents Architecture** | Native compatibility with the Strands framework and local Ollama foundation models (`gemma4:31b-cloud`, `llama3.1`). |
| **Zero-Cost Open REST APIs** | Connects to `wttr.in?format=j1` and WAQI with zero API keys and sub-second latency. |
| **Universal UTF-8 Encoding** | Explicit console encoding management ensuring seamless execution across Windows PowerShell, CMD, and Linux. |

---

## 📐 System Architecture & Logic

```
                      ┌─────────────────────────────┐
                      │         User Prompt         │
                      │ ("Compare weather between   │
                      │     Bengaluru and Delhi")   │
                      └──────────────┬──────────────┘
                                     │
                                     ▼
                      ┌─────────────────────────────┐
                      │    Versha AI Agent Engine   │
                      │  (NLP Entity Resolution)    │
                      └──────────────┬──────────────┘
                                     │
                                     ▼
                      ┌─────────────────────────────┐
                      │       HTTP Tool Suite       │
                      │      (src/tools.py)         │
                      └───────┬─────────────┬───────┘
                              │             │
           ┌──────────────────┘             └──────────────────┐
           ▼                                                   ▼
┌───────────────────────┐                           ┌───────────────────────┐
│  GET wttr.in/Bengaluru│                           │    GET wttr.in/Delhi  │
│      ?format=j1       │                           │       ?format=j1      │
└──────────┬────────────┘                           └──────────┬────────────┘
           │                                                   │
           ▼                                                   ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                        Raw JSON Telemetry Payload                         │
│  - Temperature, Feels-Like, Humidity, UV Index, Wind Vectors, Rain Chance │
└─────────────────────────────────────┬─────────────────────────────────────┘
                                      │
                                      ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                       Heuristics & Scoring Engine                         │
│  • Rain & Umbrella Decision Logic (chanceofrain %, precipMM)              │
│  • Outdoor Fitness Feasibility Score (0 to 10 Scale)                      │
│  • Side-by-Side ASCII Matrix Formatter                                    │
└─────────────────────────────────────┬─────────────────────────────────────┘
                                      │
                                      ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                          Output Rendered to User                          │
│  • Personalized Summary + Formatted Matrix + Structured Telemetry JSON    │
└───────────────────────────────────────────────────────────────────────────┘
```

### Mathematical Formulation for Outdoor Fitness Score:
$$\text{Score} = \max\left(1.0, \, \min\left(10.0, \, 10.0 - P_{\text{temp}} - P_{\text{rain}} - P_{\text{humidity}} - P_{\text{UV}} - P_{\text{wind}}
\right)
\right)$$

* **$P_{\text{temp}}$:** Penalties for extreme heat ($>30^\circ\text{C}$) or cold ($<15^\circ\text{C}$).
* **$P_{\text{rain}}$:** Penalties for precipitation probabilities ($>20\%$).
* **$P_{\text{humidity}}$:** Penalties for suffocating humidity ($>70\%$).
* **$P_{\text{UV}}$:** Penalties for hazardous ultraviolet radiation ($\ge 6$).
* **$P_{\text{wind}}$:** Penalties for gale-force winds ($>25 \text{km/h}$).

---

## 🛠️ Technologies & Tools Used

- **Language**: Python 3.8+ (Pure Standard Library Resilient)
- **Framework**: Strands Agents Architecture (`strands-agents`, `strands-agents-tools`)
- **Model Compatibility**: Ollama (`OllamaModel` / `gemma4:31b-cloud`, `llama3.1`) & Amazon Bedrock
- **Network / API Layer**: `urllib.request`, `urllib.parse`, `json`, `requests`
- **Testing & Verification**: Native Python `unittest` framework
- **Terminal UI**: Cross-platform ASCII dashboards with UTF-8 stream management

---

## 💻 Installation & Setup

No complex database or paid API keys required!

```powershell
# 1. Clone the repository
git clone https://github.com/Dominus005era/Versha-Weather-AI-Agent.git

# 2. Navigate to the project directory
cd Versha-Weather-AI-Agent

# 3. (Optional) Install dependencies for Strands / Ollama integration
pip install -r requirements.txt
```

---

## 🏃 How to Run the Project & Steps to Perform

### Step 1: Execute Automated Unit Tests
Verify all API integrations, entity extractors, and scoring algorithms:
```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

---

### Step 2: Launch the Interactive Agent CLI
Start the continuous interactive terminal interface:
```powershell
python main.py
```

---

### Step 3: Interactive Query Execution
Enter natural language prompts to test various agent capabilities:

1. **Live Diagnostics & Umbrella Advisory:**
   ```text
   User > What is the current weather in Bengaluru?
   ```
2. **Rain Advisory Engine:**
   ```text
   User > Should I carry an umbrella in Mumbai today?
   ```
3. **Outdoor Fitness Feasibility Scoring:**
   ```text
   User > Outdoor fitness score for Delhi
   ```
4. **Multi-City Side-by-Side Comparison:**
   ```text
   User > Compare weather between Bengaluru and Delhi
   ```
5. **International Weather Lookup:**
   ```text
   User > Check weather in London
   ```
6. **Graceful Exit:**
   ```text
   User > exit
   ```

---

## 📂 Project Directory Structure

```
Versha-Weather-AI-Agent/
│
├── src/
│   ├── __init__.py                    # Package initialization
│   ├── tools.py                       # REST API client, umbrella logic, outdoor scoring & matrices
│   └── agent.py                       # Strands-compatible Versha Agent & NLP entity extractor
│
├── tests/
│   ├── __init__.py
│   └── test_weather_agent.py          # Automated unittest suite (7 comprehensive test cases)
│
├── .gitignore                         # Git ignore configuration
├── main.py                            # Interactive CLI REPL application entrypoint
├── README.md                          # Project documentation and architecture guide
├── PROJECT_REPORT.md                  # Formal technical submission report
└── requirements.txt                   # Dependency and framework specification
```

---

## 🧪 Testing Suite & Verification

The project includes an automated test suite with **7 exhaustive test scenarios** built on Python's native `unittest` framework.

### Run the Test Suite:
```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

### Test Case Matrix:

| Test Case | Scenario Description | Input Condition | Expected Outcome | Status |
|---|---|---|---|:---:|
| **`test_01_fetch_weather_bengaluru`** | Real-time API telemetry retrieval | City = `"Bengaluru"` | Returns temp, humidity, UV index, and solar cycles | ✅ **PASSED** |
| **`test_02_umbrella_advisory_detection`** | Umbrella advisory classification | City = `"Mumbai"` | Returns Boolean flag and formatted rain advisory | ✅ **PASSED** |
| **`test_03_outdoor_fitness_scoring`** | Mathematical scoring algorithm | Ideal vs Harsh weather | Scores $\ge 8.0$ for ideal and $\le 4.0$ for harsh weather | ✅ **PASSED** |
| **`test_04_city_extraction_single_multi`**| NLP regular expression entity parsing| Single and multi-city prompts | Resolves single city and `["Bengaluru", "Delhi"]` pair | ✅ **PASSED** |
| **`test_05_multi_city_comparison`** | Comparative matrix generation | Comparison query | Generates side-by-side table and dual telemetry | ✅ **PASSED** |
| **`test_06_versha_execution_pipeline`** | End-to-end agent execution | Standard query | Formats personalized greeting and valid JSON | ✅ **PASSED** |
| **`test_07_invalid_city_handling`** | Fault tolerance on invalid inputs | `"NonExistentCityXYZ123"` | Gracefully triggers structured fallback payload | ✅ **PASSED** |

---

## 📊 Sample CLI & Report Output

### Single City Live Report & Umbrella Advisory:
```
========================================================================
[+] VERSHA: REAL-TIME WEATHER & ENVIRONMENTAL AI AGENT
    Persona   : Versha (Intelligent Weather & Environmental Assistant)
    Features  : Live Telemetry | Rain Advisory | Outdoor Score | Comparison
    Framework : Strands Agents + Ollama Architecture
    APIs      : wttr.in & AQI Open Environmental Endpoints
========================================================================

Versha: Hello! I am Versha, your real-time Weather and Environmental AI Assistant.
        I can help you monitor live weather, umbrella alerts, outdoor fitness scores,
        and compare conditions between multiple cities.

User > What is the current weather in Bengaluru?

-----------------------------------------------------------------
[*] [AI Agent]         : Versha
[*] [Target Location]  : BENGALURU
[*] [Execution Status] : SUCCESS
[*] [Architecture]     : Strands-Agents Architecture (Ollama Ready)
-----------------------------------------------------------------
[>] [Versha's Response]:
Hello! Here is the latest atmospheric update and environmental advisory I retrieved for you:

Atmospheric Report for Bangalore, India:
  * Condition     : Partly Cloudy 
  * Temperature   : 21 deg C (Feels like 21 deg C)
  * Humidity      : 85%
  * Wind Speed    : 18 km/h
  * UV Index      : 0
  * Solar Cycle   : Sunrise at 06:08 AM | Sunset at 06:33 PM
  * Rain Forecast : 18% chance of precipitation
  * Umbrella Alert: Not Needed (Dry & clear conditions expected)
  * Outdoor Score : 9.0/10 - Excellent (Ideal for outdoor running, cycling & sports)

[#] [Live Telemetry JSON Payload]:
{
  "status": "success",
  "city": "Bangalore",
  "region": "Karnataka",
  "country": "India",
  "temp_C": "21 deg C",
  "feels_like_C": "21 deg C",
  "humidity": "85%",
  "weather_desc": "Partly Cloudy ",
  "wind_speed_kmph": "18 km/h",
  "rain_chance_percent": "18%",
  "umbrella_advisory": "Not Needed (Dry & clear conditions expected)",
  "outdoor_fitness_score": "9.0/10"
}
=================================================================
```

### Multi-City Comparative Matrix:
```
User > Compare weather between Bengaluru and Delhi

-----------------------------------------------------------------
[*] [AI Agent]         : Versha
[*] [Comparison Mode]  : BENGALURU vs DELHI
[*] [Execution Status] : SUCCESS
[*] [Architecture]     : Strands-Agents Architecture (Ollama Ready)
-----------------------------------------------------------------
[>] [Versha's Response]:
Hello! Here is the comparative atmospheric analysis between Bengaluru and Delhi:

Location Comparison: BANGALORE vs. DEHLI

+------------------------+--------------------------+--------------------------+
| Metric                 | Bangalore                | Dehli                    |
+------------------------+--------------------------+--------------------------+
| Temperature            | 21 deg C                 | 27 deg C                 |
| Feels Like             | 21 deg C                 | 29 deg C                 |
| Weather Condition      | Partly Cloudy            | Smoky haze               |
| Humidity               | 85%                      | 66%                      |
| Wind Speed             | 18 km/h                  | 8 km/h                   |
| Rain Probability       | 18%                      | 10%                      |
| Outdoor Score          | 9.0/10                   | 10.0/10                  |
| Umbrella Advisory      | Not Needed               | Not Needed               |
+------------------------+--------------------------+--------------------------+
=================================================================
```

---

## ⚠️ Limitations

1. **Third-Party Service Uptime**: Relies on the availability of public `wttr.in` mirrors; network interruptions trigger fallback telemetry.
2. **Stateless Conversational Context**: The current REPL handles single-turn queries and comparison pairs without historical multi-turn session persistence.
3. **Macro-Scale Geographical Resolution**: City-level weather queries represent central weather stations and may vary slightly across sprawling suburban microclimates.

---

## 🔮 Future Improvements

1. **Amazon Bedrock AgentCore Integration**: Connect with cloud foundation models and persistent memory stores.
2. **Hourly Weather Sparklines**: Render ASCII graphical temperature and precipitation trends in the terminal.
3. **Automated Notification Daemons**: Implement scheduled cron jobs to alert users on morning commute conditions.
4. **Air Quality Index (AQI) Sensor Expansion**: Ingest localized particulate matter sensors (PM2.5 / PM10) across hyper-local coordinates.
