from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key requirement
SECRET_KEY = "****"  # Change this to your real key

@app.route("/")
def home():
    return """
    <h1>Welcome to LORD_SIDDHARTH API</h1>
    <p>Usage:</p>
    <pre>
    Endpoint: /api?XYZ=****
    Method: GET
    Example: https://yourexample.vercel.app/api?XYZ=****
    </pre>
    <p>Author: @LORD_SIDDHARTH</p>
    """, 200

@app.route("/api", methods=["GET"])
def api():
    key = request.args.get("XYZ")

    if key != SECRET_KEY:
        return jsonify({"error": "Unauthorized access. Invalid or missing key."}), 403

    # Example API work (replace with your logic)
    result = {"message": "Your API is working!", "author": "@LORD_SIDDHARTH"}
    return jsonify(result), 200


# For Vercel compatibility
def handler(request, *args, **kwargs):
    return app(request.environ, request.start_response)

if __name__ == "__main__":
    app.run(debug=True)
