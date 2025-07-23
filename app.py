from flask import Flask, jsonify, request
import os

PORT = os.getenv("API_PORT", "5000")

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    message = request.args.get('message')
    print(f"Received message: {message}")
    return jsonify({"message": message})

if __name__ == '__main__':
    # Важно: 0.0.0.0, чтобы Flask был доступен извне
    app.run(host="0.0.0.0", port=int(PORT))
