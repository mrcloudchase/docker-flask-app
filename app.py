# app.py
from flask import Flask
import os

app = Flask(__name__)

# Main route
@app.route("/")
def hello():
    return "I am enhancing the API"

# Healthcheck route
@app.route("/health")
def health():
    return "OK", 200

# New Route
@app.route("/new")
def new():
    return "I am enhancing the API"

if __name__ == "__main__":
    # Flask defaults to port 5000
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
