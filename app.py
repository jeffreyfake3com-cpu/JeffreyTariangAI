from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
    return "Photo uploaded successfully!"
    
    return """
    <h1>JeffreyTariang AI</h1>
    <p>AI Photo Enhancer</p>
    <p>Upload and enhance your photos.</p>
    """

if __name__ == "__main__":
    app.run()
