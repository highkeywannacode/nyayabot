from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

@app.route('/')
def home():
    return "NyayaBot is running!"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_question = data.get("question", "")

        if not user_question:
            return jsonify({"error": "No question provided"}), 400

        prompt = f"""
You are NyayaBot, an AI legal assistant trained in Indian law. Answer the following user question clearly, formally, and with accurate Indian legal context:

Question: {user_question}
"""

        response = model.generate_content(prompt)
        reply = response.text.strip()
        return jsonify({"answer": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
