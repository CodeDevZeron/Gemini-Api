import hashlib
import time
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/chat", methods=["GET"])
def chat_api():
    text = request.args.get("text")
    if not text:
        return jsonify({
            "error": "Missing text parameter",
            "api_by": "@DevZeron"
        }), 400

    timestamp = int(time.time() * 1000)
    message = f"{timestamp}:{text}:"
    sign = hashlib.sha256(message.encode()).hexdigest()

    payload = {
        "messages": [{"role": "user", "content": text}],
        "time": timestamp,
        "pass": None,
        "sign": sign
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://chat2.free2gpt.com",
        "Referer": "https://chat2.free2gpt.com"
    }

    try:
        r = requests.post("https://chat2.free2gpt.com/api/generate", json=payload, headers=headers)

        try:
            # যদি proper JSON আসে
            data = r.json()
            reply = data.get("response") or data
        except Exception:
            # যদি শুধু টেক্সট আসে
            reply = r.text.strip()

        return jsonify({
            "reply": reply,
            "api_by": "@DevZeron"
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "api_by": "@DevZeron"
        }), 500


if __name__ == "__main__":
    app.run()
