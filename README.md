# 🌦️ Versha: Real-Time Weather & Environmental AI Agent

> **Autonomous API-Driven AI Agent using Strands Framework & Open APIs**  
> *Persona: Versha (Intelligent Weather, Climate & Environmental Assistant)*  
> *Track: AWS AI Workshop & Skill Nebula Challenge*  
> **Author:** Rahul | **Architecture:** Strands Agents + Ollama + HTTP Tool Integration

---

## 📌 Overview

**Versha** is an autonomous, real-time Weather and Environmental AI Agent engineered to provide users with instantaneous climate diagnostics, smart rain/umbrella advisories, outdoor fitness feasibility scoring, and multi-city comparative analysis.

Built following the **Strands Agents framework** demonstrated in the **AWS AI Webinar** by **Skill Nebula**, Versha autonomously routes natural language requests to live open environmental REST APIs (`wttr.in` and WAQI), parses structured JSON telemetry, and delivers human-readable executive summaries.

---

## 🚀 Key Features

1. **Real-Time Live Telemetry:**
   * Ingests Temperature (°C), Feels-Like (°C), Humidity (%), Wind Vectors (km/h & direction), UV Index, and Solar Cycles (Sunrise/Sunset).
2. **☔ Smart Rain & Umbrella Advisory:**
   * Evaluates precipitation probability (`chanceofrain` %) and alerts users when umbrellas/rain gear are required.
3. **🏃‍♂️ Outdoor Activity & Fitness Feasibility Index (0–10 Score):**
   * Dynamically calculates an outdoor workout/commute suitability score based on thermal and atmospheric comfort indexes.
4. **⚖️ Multi-City Comparison & Travel Companion:**
   * Generates side-by-side terminal comparison cards when given queries like *"Compare weather between Bengaluru and Delhi"*.
5. **Strands Agents Architecture:**
   * Follows the system prompt and tool-calling pattern shown in the webinar with Ollama compatibility.
6. **Zero-Cost & Lightweight:**
   * Requires zero paid API keys and consumes minimal system resources.
7. **7/7 Automated Unit Tests:**
   * Includes complete test coverage for multi-city queries, scoring math, and error resilience.

---

## 📐 System Architecture

```
User Prompt ("Compare weather between Bengaluru and Delhi")
       │
       ▼
[Versha AI Agent (Strands Pattern)]
       │
       ├─► Multi-Entity Resolver ("Bengaluru", "Delhi")
       │
       ├─► HTTP API Tool (GET https://wttr.in/Bengaluru?format=j1)
       ├─► HTTP API Tool (GET https://wttr.in/Delhi?format=j1)
       │     │
       │     ▼
       │  [Environmental Telemetry Parser]
       │  - Thermal Profile (Temp, Feels-like)
       │  - Precipitation & Umbrella Alert Engine
       │  - Outdoor Fitness Feasibility Algorithm (0-10)
       │     │
       ▼     ▼
Side-by-Side Comparison Card & Live JSON Telemetry
```

---

## 🧪 Quick Start & Verification

### 1. Run Automated Test Suite
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 2. Launch Interactive Terminal Assistant
```bash
python main.py
```

---

## 🎥 Demonstration Steps for LinkedIn Video

1. Open your terminal in the `Versha-Weather-AI-Agent` directory.
2. Run the test suite:
   ```bash
   python -m unittest discover -s tests -p "test_*.py" -v
   ```
3. Start Versha:
   ```bash
   python main.py
   ```
4. Enter sample queries:
   * `What is the current weather in Bengaluru?` *(Demonstrates live telemetry & umbrella alert)*
   * `Should I carry an umbrella in Mumbai today?` *(Demonstrates rain advisory engine)*
   * `Outdoor fitness score for Delhi` *(Demonstrates 0-10 activity feasibility score)*
   * `Compare weather between Bengaluru and Delhi` *(Demonstrates side-by-side comparison table)*
   * `exit`
