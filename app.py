from flask import Flask, request, jsonify, render_template
import re
from repositories.user_repository import InMemoryUserRepository

app = Flask(__name__)
user_repository = InMemoryUserRepository()

@app.route('/')
def index():
    return render_template('index.html')

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_cpf(cpf):
    return re.match(r"\d{11}$", cpf)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()

    # Validações
    if not data.get('nome'):
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    if not data.get('cpf') or not validar_cpf(data['cpf']):
        return jsonify({'erro': 'CPF inválido (deve conter 11 dígitos numéricos)'}), 400
    if not data.get('email') or not validar_email(data['email']):
        return jsonify({'erro': 'E-mail inválido'}), 400
    if not data.get('senha') or len(data['senha']) < 6:
        return jsonify({'erro': 'Senha deve ter no mínimo 6 caracteres'}), 400
    if data.get('atividade') not in ['caminhada', 'pedalada', 'ambos']:
        return jsonify({'erro': 'Tipo de atividade inválido'}), 400

    # Verificar se usuário já existe
    if user_repository.find_by_email(data['email']):
        return jsonify({'erro': 'E-mail já cadastrado'}), 400
    if user_repository.find_by_cpf(data['cpf']):
        return jsonify({'erro': 'CPF já cadastrado'}), 400

    usuario = {
        'nome': data['nome'],
        'cpf': data['cpf'],
        'email': data['email'],
        'senha': data['senha'],
        'atividade': data['atividade'],
        'avaliacoes': []
    }

    user_repository.create(usuario)

    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
