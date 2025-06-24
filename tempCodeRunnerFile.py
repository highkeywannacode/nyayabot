from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Load your Gemini API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return "NyayaBot (Gemini) is online!"

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question")

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    system_prompt = (
        "You are NyayaBot, an AI assistant trained on Indian law.\n"
        "Answer user legal questions in a formal, clear, and concise tone.\n"
        "Always include this disclaimer: 'This is general legal information, not legal advice. Please consult a lawyer for specific cases.'"
    )

    try:
        model = genai.GenerativeModel("gemini-pro")
        convo = model.start_chat(history=[])
        convo.send_message(f"{system_prompt}\nUser: {user_question}")
        reply = convo.last.text

        return jsonify({"answer": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
