from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.form
    name = data.get('name', 'Anonymous')
    message = data.get('message', '')
    if message:
        messages.append({'name': name, 'message': message})
        return jsonify({'status': 'Message sent successfully'}), 200
    else:
        return jsonify({'status': 'Failed to send message'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)


if __name__ == "__main__":
    app.run(host="192.168.119.231", port=5000, debug=True)
