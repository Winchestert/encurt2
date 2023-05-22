from flask import Flask

app = Flask(__name__)


def index():
    return "Bem-vindo à minha API!"

@app.route("/users", methods=["GET"])
def list_users():
    return "Lista de usuários"

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return "Detalhes do usuário {user_id}"

if __name__ == "__main__":
    app.run(debug=True)


