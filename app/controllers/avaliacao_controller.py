from flask import Blueprint, request, jsonify
from app.models.user import User, Avaliacao
from app import db

avaliacao_bp = Blueprint('avaliacao', __name__)

@avaliacao_bp.route('/avaliacao', methods=['POST'])
def criar_avaliacao():
    data = request.get_json()
    
    # Validate required fields
    if 'id_avaliador' not in data:
        return jsonify({'erro': 'ID do avaliador é obrigatório'}), 400
    
    if 'id_avaliado' not in data:
        return jsonify({'erro': 'ID do avaliado é obrigatório'}), 400
    
    # Check if users exist
    avaliador = User.query.get(data['id_avaliador'])
    avaliado = User.query.get(data['id_avaliado'])
    
    if not avaliador or not avaliado:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    # Check if it's a self-evaluation
    if data['id_avaliador'] == data['id_avaliado']:
        return jsonify({'erro': 'Usuário não pode se autoavaliar'}), 400
    
    # Check if users share the same activity
    if avaliador.atividade != avaliado.atividade:
        return jsonify({'erro': 'Compartilhamento da mesma rota é obrigatório'}), 400
    
    # Validate rating
    if 'nota' not in data:
        return jsonify({'erro': 'Nota é obrigatória'}), 400
    
    if not isinstance(data['nota'], int) or data['nota'] < 1 or data['nota'] > 5:
        return jsonify({'erro': 'Nota deve ser entre 1 e 5'}), 400
    
    # Validate evaluation type
    if 'tipo_avaliacao' not in data or data['tipo_avaliacao'] not in ['comportamento', 'seguranca', 'pontualidade']:
        return jsonify({'erro': 'Tipo de avaliação inválido'}), 400
    
    # Create new evaluation
    avaliacao = Avaliacao(
        id_avaliador=data['id_avaliador'],
        id_avaliado=data['id_avaliado'],
        nota=data['nota'],
        comentario=data.get('comentario', ''),
        tipo_avaliacao=data['tipo_avaliacao']
    )
    
    db.session.add(avaliacao)
    db.session.commit()
    
    return jsonify({'mensagem': 'Avaliação registrada com sucesso'}), 201 