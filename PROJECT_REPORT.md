# 📋 Technical Project Report & Architecture Specification

## 🌦️ Versha: Real-Time Weather & Environmental AI Agent
> **Autonomous Decision-Intelligence AI Agent with Multi-City Comparative Telemetry**  
> **Program:** AWS AI & Cloud AI Agent Workshop — Skill Nebula  
> **Author:** Rahul  
> **Framework:** Python 3.8+, Strands Agents Architecture, REST Open APIs  
> **Repository:** [https://github.com/Dominus005era/Versha-Weather-AI-Agent](https://github.com/Dominus005era/Versha-Weather-AI-Agent)

---

## 1. Executive Summary & Abstract

In contemporary artificial intelligence engineering, autonomous agents are shifting from passive text generation toward active, tool-augmented systems capable of interacting with real-world APIs and live telemetry streams. 

**Versha** is an autonomous, lightweight AI Agent built to provide instantaneous atmospheric diagnostics, proactive rain and umbrella advisories, outdoor fitness feasibility scoring, and multi-city comparative analysis. Modeled after the architectural principles demonstrated in the **AWS AI Webinar** by **Skill Nebula**, Versha integrates the **Strands Agents framework**, natural language entity extraction, and zero-authentication public REST endpoints (`wttr.in` and WAQI) to deliver structured climate telemetry with 100% zero-cost standard library resilience.

---

## 2. Problem Statement & Motivation

### 2.1 The Problem
Standard large language models (LLMs) suffer from **knowledge cutoff limitations** and **hallucinations** when asked about transient, real-time conditions such as live weather, precipitation probabilities, or local atmospheric metrics. 

### 2.2 Project Objectives
1. **Tool-Augmented Intelligence**: Equip the agent with dynamic HTTP tooling to bridge LLM reasoning with live REST endpoints.
2. **Predictive Decision Support**: Implement algorithmic scoring for umbrella advisories and an Outdoor Fitness Feasibility Index (0–10 score).
3. **Multi-Entity Comparative Intelligence**: Parse natural language comparative queries (e.g., *"Compare weather between Bengaluru and Delhi"*) and generate side-by-side diagnostic cards.
4. **Multi-Metric Telemetry Extraction**: Ingest and structure complex JSON payloads into core metrics:
   - **Thermal Profile:** Ambient Temperature (°C) and "Feels-Like" index.
   - **Atmospheric Dynamics:** Relative Humidity (%), Barometric Pressure (hPa), Visibility (km).
   - **Wind & Solar Vectors:** Wind Speed (km/h), Wind Direction, UV Index, Sunrise, and Sunset timings.
5. **Zero Setup Friction**: Maintain zero external paid API dependencies while achieving 100% automated test coverage.

---

## 3. System Architecture & Workflow

```
+-----------------------------------------------------------------------+
|                                USER                                   |
|       Prompt: "Compare weather between Bengaluru and Delhi"           |
+-----------------------------------┬-----------------------------------+
                                    │
                                    ▼
+-----------------------------------------------------------------------+
|                    VERSHA AI AGENT ENGINE (src/agent.py)              |
|  - Persona: Versha (System Prompt & Persona Definition)               |
|  - Entity Resolver: Isolates Target Cities (["Bengaluru", "Delhi"])   |
|  - Dispatcher: Executes Tool Calls for Identified Locations           |
+-----------------------------------┬-----------------------------------+
                                    │
                                    ▼
+-----------------------------------------------------------------------+
|                     HTTP TOOL SUITE (src/tools.py)                    |
|  - Request Engine: urllib.request to https://wttr.in/<city>?format=j1 |
|  - Umbrella Engine: Evaluates chanceofrain & precipMM                 |
|  - Fitness Algorithm: Evaluates Temp, Humidity, UV, Wind (0-10 Score) |
+-----------------------------------┬-----------------------------------+
                                    │
                                    ▼
+-----------------------------------------------------------------------+
|                      LIVE REST API (wttr.in / WAQI)                   |
|  - Returns comprehensive multi-layer JSON telemetry                   |
+-----------------------------------┬-----------------------------------+
                                    │
                                    ▼
+-----------------------------------------------------------------------+
|                    TELEMETRY PARSER & FORMATTER                       |
|  - Generates: Comparative ASCII Matrix + Structured JSON Telemetry    |
+-----------------------------------┬-----------------------------------+
                                    │
                                    ▼
+-----------------------------------------------------------------------+
|                       OUTPUT DELIVERY TO USER                         |
|  - Interactive Terminal ASCII Dashboard & JSON Telemetry Inspector    |
+-----------------------------------------------------------------------+
```

---

## 4. Algorithmic Design & Heuristics Engine

### 4.1 Rain & Umbrella Advisory Engine
The agent evaluates the probability of precipitation (`chanceofrain` %) and precipitation volume (`precipMM`) from the hourly forecast array:
* **$\text{Rain Probability} \ge 50\%$ or Rain/Drizzle keywords**: `Required (High likelihood of precipitation)`
* **$25\% \le \text{Rain Probability} < 50\%$**: `Recommended (Partly overcast / light drizzle possible)`
* **$\text{Rain Probability} < 25\%$**: `Not Needed (Dry & clear conditions expected)`

### 4.2 Outdoor Fitness & Commute Feasibility Algorithm
The agent computes an explainable **Outdoor Fitness Score** (range: 1.0 to 10.0) using a multi-factor penalty function:

$$\text{Score} = 10.0 - P_{\text{temp}} - P_{\text{rain}} - P_{\text{humidity}} - P_{\text{UV}} - P_{\text{wind}}$$

* **Temperature Penalty ($P_{\text{temp}}$):**
  * $T > 35^\circ\text{C} \implies -3.5$
  * $30^\circ\text{C} < T \le 35^\circ\text{C} \implies -2.0$
  * $T < 10^\circ\text{C} \implies -2.5$
  * $10^\circ\text{C} \le T < 15^\circ\text{C} \implies -1.0$
  * $15^\circ\text{C} \le T \le 26^\circ\text{C} \implies 0.0$ *(Optimal)*
* **Rain Penalty ($P_{\text{rain}}$):**
  * $\text{Rain} > 70\% \implies -4.0$
  * $40\% < \text{Rain} \le 70\% \implies -2.5$
  * $20\% < \text{Rain} \le 40\% \implies -1.0$
* **Humidity Penalty ($P_{\text{humidity}}$):**
  * $H > 85\% \implies -2.0$
  * $70\% < H \le 85\% \implies -1.0$
* **UV Penalty ($P_{\text{UV}}$):**
  * $\text{UV} \ge 8 \implies -1.5$
  * $6 \le \text{UV} < 8 \implies -0.5$
* **Wind Penalty ($P_{\text{wind}}$):**
  * $W > 35 \text{km/h} \implies -2.0$
  * $25 \text{km/h} < W \le 35 \text{km/h} \implies -1.0$

**Classification Output:**
* **$\ge 8.0$:** *Excellent (Ideal for outdoor running, cycling & sports)*
* **$6.0 - 7.9$:** *Moderate (Good for walking & light commute; stay hydrated)*
* **$4.0 - 5.9$:** *Fair (Sub-optimal conditions; outdoor workouts not recommended)*
* **$< 4.0$:** *Poor (Unfavorable weather; indoor activities recommended)*

---

## 5. Technical Implementation Details

### 5.1 Tooling & Data Layer (`src/tools.py`)
* **`fetch_weather_data(city)`**: Initiates an HTTP GET request to `https://wttr.in/<city>?format=j1`. Extracts thermal, atmospheric, wind, and astronomical vectors.
* **`calculate_outdoor_score(...)`**: Implements the multi-factor heuristics scoring engine.
* **`format_city_comparison(c1, c2)`**: Renders a side-by-side comparative ASCII matrix.

### 5.2 Agent Logic & Persona (`src/agent.py`)
* **Persona Definition**: Configured with a system prompt establishing Versha as a friendly, intelligent environmental assistant.
* **Entity Extraction (`extract_cities`)**: Regular expression engine parsing comparison phrases (`"compare ... and ..."`, `"... vs ..."`).
* **Strands & Ollama Readiness**: Built with class interfaces compatible with `strands-agents` and `OllamaModel` (`model_id="gemma4:31b-cloud"`, `host="http://127.0.0.1:11434"`), while maintaining standalone runtime execution.

### 5.3 Interactive Interface (`main.py`)
* Implements a continuous REPL (Read-Eval-Print Loop) displaying Versha's response and formatted JSON payload side-by-side.
* Includes explicit console re-encoding (`sys.stdout.reconfigure(encoding="utf-8")`) ensuring universal compatibility across Windows PowerShell, CMD, and Linux terminals.

---

## 6. Automated Verification & Unit Test Suite

The project includes an automated test suite located in `tests/test_weather_agent.py`. All 7 test cases pass with a 100% success rate:

```
test_01_fetch_weather_bengaluru ............................... PASSED
test_02_umbrella_advisory_detection ........................... PASSED
test_03_outdoor_fitness_scoring_algorithm ..................... PASSED
test_04_city_extraction_single_and_multi ...................... PASSED
test_05_multi_city_comparison_pipeline ........................ PASSED
test_06_versha_execution_pipeline_and_persona ................. PASSED
test_07_invalid_city_graceful_handling ........................ PASSED

----------------------------------------------------------------------
Ran 7 tests in 3.65s | Status: OK (All Tests Passed)
```

---

## 7. Architectural Decisions & Technical Rationale

### 7.1 Why an Autonomous AI Agent vs. a Rigid CLI Script?
A standard script requires rigid syntax (e.g., `script.py --city Bengaluru`). An **AI Agent** accepts unstructured natural language, extracts target geographical entities, selects tools dynamically, and contextualizes raw numbers into actionable advice (e.g., umbrella alerts and workout safety).

### 7.2 Why the Strands Agents Framework?
The **Strands Agents framework** provides a standardized interface for system prompts, modular tool registration (`tools=[...]`), and interoperability with local models (**Ollama**) or cloud models (**AWS Bedrock**).

### 7.3 Why `wttr.in?format=j1`?
`wttr.in` is an open, zero-authentication meteorological endpoint. Appending `format=j1` returns machine-readable JSON data containing complete astronomical, thermal, and meteorological telemetry with sub-second response times.

---

## 8. Conclusion & Future Roadmap

Versha demonstrates how autonomous agent frameworks combined with open public APIs can deliver zero-cost, high-utility decision intelligence tools. 

**Future Roadmap:**
* Integration with Amazon Bedrock AgentCore for multi-turn memory persistence.
* Expansion of hourly precipitation charts using ASCII sparklines.
* Automated scheduled notifications for morning commute planning.
