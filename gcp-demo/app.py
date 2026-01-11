from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Google Cloud Run!"

if __name__ == "__main__":
    # Cloud Run sẽ tự set PORT
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
