from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"  # Change to your local model name

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json(force=True)
    prompt = data.get('prompt', '')

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload)
        resp.raise_for_status()
        answer = resp.json().get('response', '')
    except Exception as e:
        answer = f"Error contacting LLM: {e}"

    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(port=5000)
