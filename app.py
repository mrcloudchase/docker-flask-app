# app.py
from flask import Flask, request, jsonify
import os
from transformers import pipeline


app = Flask(__name__)

# Main route
@app.route("/")
def hello():
    return "Welcome to my Flask app!"

# Healthcheck route
@app.route("/health")
def health():
    return "OK", 200

# Load the model
generator = pipeline('text-generation', model='gpt2')

# LLM endpoint
@app.route("/generate", methods=["POST"])
def generate_text():
    # Get the input text from the request
    input_data = request.json
    input_text = input_data.get("text", "")

    # Generate text using the model
    results = generator(input_text, max_length=50, num_return_sequences=1)

    # Return the generated text
    return jsonify(results)


if __name__ == "__main__":
    # Flask defaults to port 5000
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
