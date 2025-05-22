from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        atividade = request.form.get('atividade', 'caminhada')  # Default to caminhada if not provided
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        
        user = User(username=username, email=email, atividade=atividade)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth_bp.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    
    # Validate required fields
    if not data:
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    
    if 'nome' not in data:
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    
    if 'email' not in data:
        return jsonify({'erro': 'E-mail inválido'}), 400
    
    if 'cpf' not in data:
        return jsonify({'erro': 'CPF inválido'}), 400
    
    if 'senha' not in data or len(data['senha']) < 6:
        return jsonify({'erro': 'Senha deve ter pelo menos 6 caracteres'}), 400
    
    if 'atividade' not in data or data['atividade'] not in ['caminhada', 'pedalada', 'ambos']:
        return jsonify({'erro': 'Atividade inválida'}), 400
    
    if 'preferencias' not in data:
        return jsonify({'erro': 'Preferências são obrigatórias'}), 400
    
    if 'horario' not in data['preferencias'] or data['preferencias']['horario'] not in ['manha', 'tarde', 'noite']:
        return jsonify({'erro': 'Horário inválido'}), 400
    
    if 'frequencia' not in data['preferencias'] or data['preferencias']['frequencia'] not in ['diaria', 'semanal', 'mensal']:
        return jsonify({'erro': 'Frequência inválida'}), 400
    
    # Create new user
    user = User(
        nome=data['nome'],
        email=data['email'],
        cpf=data['cpf'],
        senha=data['senha'],
        atividade=data['atividade'],
        preferencias=data['preferencias']
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201 