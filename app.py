from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# Implementação do UserRepository
class UserRepository:
    def __init__(self):
        self._usuarios = []
        self._next_id = 1  # Contador para IDs automáticos
    
    def add(self, usuario):
        """Adiciona um novo usuário com ID automático"""
        usuario['id'] = self._next_id
        self._usuarios.append(usuario)
        self._next_id += 1
        return usuario
    
    def get_by_id(self, id):
        """Obtém usuário por ID"""
        for user in self._usuarios:
            if user.get('id') == id:
                return user
        return None
    
    def get_by_email(self, email):
        """Obtém usuário por email"""
        for user in self._usuarios:
            if user.get('email') == email:
                return user
        return None
    
    def get_all(self):
        """Retorna todos os usuários"""
        return self._usuarios.copy()

# Instância global do repositório
user_repo = UserRepository()

# Rotas da aplicação
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
    if user_repo.get_by_email(data['email']):
        return jsonify({'erro': 'E-mail já cadastrado'}), 400
    if not data.get('senha') or len(data['senha']) < 6:
        return jsonify({'erro': 'Senha deve ter no mínimo 6 caracteres'}), 400
    if data.get('atividade') not in ['caminhada', 'pedalada', 'ambos']:
        return jsonify({'erro': 'Tipo de atividade inválido'}), 400

    usuario = {
        'nome': data['nome'],
        'cpf': data['cpf'],
        'email': data['email'],
        'senha': data['senha'],  # Em produção, armazene apenas o hash!
        'atividade': data['atividade'],
        'avaliacoes': []
    }

    user_repo.add(usuario)
    return jsonify({
        'mensagem': 'Usuário cadastrado com sucesso!',
        'id': usuario['id']
    }), 201

@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    usuario = user_repo.get_by_id(user_id)
    if usuario:
        return jsonify(usuario)
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(user_repo.get_all())

if __name__ == '__main__':
    app.run(debug=True)

# --- Compatibilidade com testes existentes ---
usuarios = user_repo._usuarios  # Expõe a lista interna para os testes
