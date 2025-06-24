from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace with your actual Gemini API Key
GOOGLE_API_KEY = "AIzaSyDm3M6aaZaeZua6v_fFNWIl7w96Cmryd50"
genai.configure(api_key=GOOGLE_API_KEY)

# Correct model name
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
    app.run(debug=True)
