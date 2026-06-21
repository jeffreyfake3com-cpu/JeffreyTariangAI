from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>JeffreyTariang AI</h1>
    <p>AI Photo Enhancer</p>
    <p>Upload and enhance your photos.</p>
    """

if __name__ == "__main__":
    app.run()
