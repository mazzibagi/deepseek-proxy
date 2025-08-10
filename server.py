from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")  # Ключ из Render Secrets
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/v1/chat/completions", methods=["POST"])
def proxy():
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        data = request.get_json()
        resp = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "DeepSeek Proxy is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
