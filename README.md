⚽ Football Tactical AI App
This project is a simple full-stack AI application designed to help football coaches analyze opponents and generate tactical insights.

https://football-ai-app-eta.vercel.app/

🚀 Features
Input opponent tactics as text
AI-generated tactical analysis using LLM
History tracking of past queries

⚙️ Tech Stack
1. Backend
FastAPI
OpenRouter API
Model: gpt-oss-120b (free tier)
2. Frontend
HTML + Tailwind CSS
Vanilla JavaScript
3. Database
SQLite (local history storage)

🔄 How It Works
User inputs opponent details
Request sent to FastAPI backend
Backend calls OpenRouter LLM
Model generates tactical insights
Response displayed in UI

🌍 Deployment
Backend → Render
Frontend → Vercel

🧠 Note
The app uses a free LLM model via OpenRouter, so response time may vary depending on latency.
