from flask import Blueprint, request, jsonify
from app.models.local import Local
from app import db

local_bp = Blueprint('local', __name__)

@local_bp.route('/cadastrar_local', methods=['POST'])
def cadastrar_local():
    data = request.get_json()
    
    # Validate required fields
    if not data:
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    
    if 'nome' not in data:
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    
    if 'endereco' not in data or not isinstance(data['endereco'], str):
        return jsonify({'erro': 'Endereço inválido'}), 400
    
    if 'proximidade' not in data:
        return jsonify({'erro': 'Proximidade é obrigatória'}), 400
    
    if 'numero_incidentes' not in data or not isinstance(data['numero_incidentes'], int) or data['numero_incidentes'] < 0:
        return jsonify({'erro': 'Número de incidentes deve ser um número inteiro >= 0'}), 400
    
    if 'relatos' not in data or not isinstance(data['relatos'], list):
        return jsonify({'erro': 'Relatos devem ser enviados como uma lista'}), 400
    
    if 'coordenadas' not in data:
        return jsonify({'erro': 'Coordenadas são obrigatórias'}), 400
    
    if not isinstance(data['coordenadas'].get('latitude'), (int, float)) or not isinstance(data['coordenadas'].get('longitude'), (int, float)):
        return jsonify({'erro': 'Coordenadas inválidas'}), 400
    
    if 'tipo_local' not in data or data['tipo_local'] not in ['estacionamento', 'parque', 'praça', 'rua']:
        return jsonify({'erro': 'Tipo de local inválido'}), 400
    
    # Calculate security score
    nota_seguranca = max(0, 10 - data['numero_incidentes'])
    
    # Create new local
    local = Local(
        nome=data['nome'],
        endereco=data['endereco'],
        proximidade=data['proximidade'],
        numero_incidentes=data['numero_incidentes'],
        relatos=data['relatos'],
        coordenadas=data['coordenadas'],
        tipo_local=data['tipo_local'],
        nota_seguranca=nota_seguranca
    )
    
    db.session.add(local)
    db.session.commit()
    
    return jsonify({
        'mensagem': 'Local cadastrado com sucesso!',
        'local': {
            'id': local.id,
            'nome': local.nome,
            'nota_seguranca': local.nota_seguranca
        }
    }), 201 