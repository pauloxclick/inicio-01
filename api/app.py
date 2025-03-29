from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Chave secreta para JWT
jwt = JWTManager(app)

# Dados de usuário fictícios
users = {
    "admin": "password"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"msg": "Access granted"})

if __name__ == '__main__':
    app.run(debug=True)