from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (list of dictionaries)
users = [
    {"id": 1, "name": "Aditya Raj", "email": "aditya@example.com"},
    {"id": 2, "name": "Bimla Devi", "email": "bimla@example.com"}
]

# 1. GET - Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# 2. GET - Retrieve a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# 3. POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    # request.json extracts the incoming JSON data sent by the client
    data = request.json
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Bad Request. Name and Email are required."}), 400
    
    # Generate a unique ID
    new_id = users[-1]['id'] + 1 if users else 1
    
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# 4. PUT - Update an existing user entirely
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    
    return jsonify(user), 200

# 5. DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted successfully"}), 200

# How to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)