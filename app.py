from flask import Flask, request, jsonify, render_template
from controllers.user_controller import UserController

app = Flask(__name__)
user_controller = UserController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    return jsonify(*user_controller.cadastrar_usuario(data))

if __name__ == '__main__':
    app.run(debug=True)
