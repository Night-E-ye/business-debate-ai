from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re

app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"


# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = re.sub(r'<\|.*?\|>', '', text)
    text = text.replace('*', '').replace('_', '').strip()
    if text and text[-1] not in '.!?':
        text += '.'
    return text


# ---------------- DEBATE PROMPT ----------------
def get_debate_prompt(role, turn_count):
    if role == "for":
        name = "Alex"
        belief = (
            "You strongly believe Marketing drives growth. "
            "Without demand creation, sales efficiency fails. "
            "You focus on brand, CAC reduction, and long-term scale."
        )
    else:
        name = "Sam"
        belief = (
            "You strongly believe Sales drives reality. "
            "Revenue validates strategy, not awareness. "
            "You focus on conversion, cash flow, and execution."
        )

    base = (
        f"You are {name}, a senior business executive.\n"
        f"{belief}\n"
        "Rules:\n"
        "- Max 3 sentences\n"
        "- Directly challenge the other side\n"
        "- No agreement unless forced\n"
        "- Business only"
    )

    if turn_count == 0:
        return f"{base}\nOpen with a bold claim."
    else:
        return f"{base}\nRespond directly to the opponent."


# ---------------- DEBATE ENDPOINT ----------------
@app.route("/debate", methods=["POST"])
def debate():
    data = request.json
    role = data.get("role")
    history = data.get("history", [])
    turn_count = len(history)

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": get_debate_prompt(role, turn_count)}
        ] + history,
        "options": {
            "temperature": 0.9,
            "repeat_penalty": 1.9,
            "num_predict": 200
        },
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=40)
    text = clean_text(response.json()["message"]["content"])

    return jsonify({
        "agentName": "Alex" if role == "for" else "Sam",
        "message": text,
        "nextRole": "against" if role == "for" else "for"
    })


# ---------------- CONCLUSION ENDPOINT ----------------
@app.route("/conclusion", methods=["POST"])
def conclusion():
    history = request.json.get("history", [])

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a neutral strategy moderator.\n\n"
                    "Task:\n"
                    "1. Extract Marketing’s strongest point.\n"
                    "2. Extract Sales’ strongest point.\n"
                    "3. Produce ONE shared operating model both sides accept.\n\n"
                    "Rules:\n"
                    "- Concrete\n"
                    "- Actionable\n"
                    "- No generic language\n"
                    "- Output only the final conclusion"
                )
            }
        ] + history,
        "options": {
            "temperature": 0.6,
            "num_predict": 250
        },
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=40)
    text = clean_text(response.json()["message"]["content"])

    return jsonify({"conclusion": text})


if __name__ == "__main__":
    app.run(port=5000)
