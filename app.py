from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, from Python Flask app!</p>"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Default to 5000 if PORT not set
    app.run(host="0.0.0.0", port=port)