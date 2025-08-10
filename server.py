from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")  

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    data = await request.json()
    r = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        },
        json=data
    )
    return r.json()
