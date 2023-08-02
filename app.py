from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista dos 10 principais Vingadores
users = [
    {"id": 1, "name": "Tony Stark", "age": 35},
    {"id": 2, "name": "Steve Rogers", "age": 100},
    {"id": 3, "name": "Natasha Romanoff", "age": 32},
    {"id": 4, "name": "Bruce Banner", "age": 45},
    {"id": 5, "name": "Clint Barton", "age": 40},
    {"id": 6, "name": "Thor Odinson", "age": 1500},
    {"id": 7, "name": "Wanda Maximoff", "age": 29},
    {"id": 8, "name": "Scott Lang", "age": 40},
    {"id": 9, "name": "Peter Parker", "age": 23},
    {"id": 10, "name": "Carol Danvers", "age": 35},
]


# Rota para listar todos os Vingadores
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# Rota para obter um Vingador por ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "Vingador não encontrado"}), 404


# Rota para adicionar um novo Vingador
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"message": "Dados inválidos"}), 400

    user = {"id": len(users) + 1, "name": data["name"], "age": data["age"]}
    users.append(user)
    return jsonify(user), 201


# Rota para atualizar um Vingador existente
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        return jsonify({"message": "Vingador não encontrado"}), 404

    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"message": "Dados inválidos"}), 400

    user["name"] = data["name"]
    user["age"] = data["age"]
    return jsonify(user)


# Rota para deletar um Vingador
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "Vingador deletado"}), 200


if __name__ == "__main__":
    app.run()
