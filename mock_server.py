from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "testuser": "testpass"
}

mock_db = {}

@auth.get_password
def get_pw(username):
    return users.get(username)

@app.route('/v1/poweroutage', methods=['POST'])
@auth.login_required
def report_power_outage():
    data = request.get_json()
    new_id = str(len(mock_db) + 1)
    data["id"] = new_id
    mock_db[new_id] = data
    return jsonify(data), 201

@app.route('/v1/poweroutage', methods=['GET'])
@auth.login_required
def get_all():
    return jsonify(list(mock_db.values()))

@app.route('/v1/poweroutage/<id>', methods=['GET'])
@auth.login_required
def get_by_id(id):
    if id in mock_db:
        return jsonify(mock_db[id])
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)