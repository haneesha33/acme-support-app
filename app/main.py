import logging
import os

from flask import Flask, jsonify

app = Flask(__name__)
logger = logging.getLogger("acme")


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", "8080")))
