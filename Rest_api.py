from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route("/posts")
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    return jsonify(response.json()), response.status_code

@app.route("/posts", methods=["POST"])
def create_post():
    payload = request.json  # JSON body sent by client
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    return jsonify(response.json()), response.status_code
@app.route("/posts/<int:id>", methods=["PUT"])
def update_post(id):
    payload = request.json
    response = requests.put(f"{BASE_URL}/posts/{id}", json=payload)
    return jsonify(response.json()), response.status_code
@app.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    response = requests.delete(f"{BASE_URL}/posts/{id}")
    if response.status_code == 200:
        return jsonify({"message": f"Post {id} deleted successfully"}), 200
    return jsonify({"error": "Failed to delete post"}), response.status_code


if __name__ == "__main__":
    app.run(debug = True)