from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv
from database import init_db, save_query

# Load API key
load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("OPENROUTER_API_KEY")
print("API_KEY:", API_KEY)

# Create app
app = FastAPI()
init_db()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Basic test route
@app.get("/")
def home():
    return {"message": "Backend running"}

# Function to call OpenRouter
def get_tactics(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-120b:free",
        "messages": [
            {"role": "system", "content": "You are a football tactical analyst."},
            {"role": "user", "content": prompt}
        ]
    }
        
    response = requests.post(url, headers=headers, json=data)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    res_json = response.json()

    if "choices" in res_json:
        return res_json["choices"][0]["message"]["content"]
    else:
        return f"API Error: {res_json}"

# API endpoint
@app.post("/analyze")
def analyze(input_text: str = Form(...)):
    result = get_tactics(input_text)
    save_query(input_text, result)
    return {"input": input_text, "tactics": result}

@app.get("/history")
def get_history():
    import sqlite3
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()

    conn.close()

    return {"history": rows}