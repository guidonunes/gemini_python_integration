# 🎮 Gemini Python Integration  
### **AI-Driven Video Game Recommendation Engine**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)  
![Gemini](https://img.shields.io/badge/Google%20Gemini-API-green?style=for-the-badge&logo=google)  
![AI](https://img.shields.io/badge/AI-Recommendation%20System-purple?style=for-the-badge)

---

## 📖 Overview

**gemini_python_integration** is an **AI-powered recommendation engine** that analyzes user input, performs **sentiment analysis**, and suggests **video games** using **Google Gemini’s LLM models**.

The project includes:

- Automatic **model selection** based on input size  
- **Token counting** and **cost estimation**  
- **Categorization module** to interpret user prompts  
- A clean, extensible **modular structure**  
- Interaction flow via **main.py**

Perfect for learning how to integrate Google Gemini into Python workflows or for building more advanced content recommendation systems.

---

## 🧠 Features

### ✔️ Dynamic Gemini Model Selection  
Automatically selects the best Gemini model depending on prompt size and complexity.

### ✔️ User Sentiment Categorizer  
Analyzes user input to detect genre preference, tone, and intent.

### ✔️ Token Usage & Cost Calculator  
Accurately estimates token consumption and API cost per request.

### ✔️ Modular Architecture  
Each module has a single responsibility:

- categorizer.py – Sentiment/game genre categorization  
- model_selector.py – Adaptive Gemini model selector  
- token_counter.py – Token + cost computation  
- main.py – User interaction & system orchestration  

### ✔️ Data Folder  
Contains datasets or configuration files used during recommendation.

---

## 📂 Project Structure

```
gemini_python_integration/
│
├── data/                   # Datasets, prompts, resources
├── categorizer.py          # Sentiment & genre categorization
├── main.py                 # Entry point: runs the recommendation engine
├── model_selector.py       # Dynamic Gemini model selector
├── token_counter.py        # Token counting & cost calculations
├── requirements.txt        # Project dependencies
└── .gitignore
```

---

## 🚀 How It Works

1. User enters a sentence describing mood, preferences, or play style  
2. categorizer.py processes the sentiment & extracts game-relevant traits  
3. model_selector.py chooses the optimal Gemini model  
4. token_counter.py estimates inference cost  
5. Gemini generates **personalized game recommendations**  
6. Output is displayed via the CLI

---

## 📌 Future Improvements (optional section)

1. Add multiplayer or platform-specific recommendations

2. Introduce memory for long-term user profiles

3. Add a web UI (Flask/React)

4. Integrate Steam, Metacritic, or IGDB APIs for real-time game data
