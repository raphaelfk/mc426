from flask import Flask, request, jsonify

from app import usuarios

app = Flask(__name__)

@app.route('/avaliacao', methods=['POST'])
def avaliar():
    data = request.get_json()

    if data.get('id_avaliador') is None:
        return jsonify({'erro': 'ID do avaliador é obrigatório'}), 400
    if data.get('id_avaliado') is None:
        return jsonify({'erro': 'ID do avaliado é obrigatório'}), 400
    
    id_avaliador = data.get('id_avaliador')
    id_avaliado = data.get('id_avaliado')
    
    if id_avaliador == id_avaliado:
        return jsonify({'erro': 'Usuário não pode se autoavaliar'}), 400

    try:
        avaliador = usuarios[id_avaliador]
        avaliado = usuarios[id_avaliado]
    except IndexError:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    if avaliador['atividade'] != avaliado['atividade']:
        return jsonify({'erro': 'Compartilhamento da mesma rota é obrigatório'}), 400

    nota = data.get('nota')
    valido, erro = valida_nota(data, nota)
    if not valido:
        return jsonify({'erro': erro}), 400
        
    # if not data.get('nota'):
    #     return jsonify({'erro': 'Nota é obrigatória'}), 400
    # elif not isinstance(nota, int) or (nota < 1) or (nota > 5):
    #     return jsonify({'erro': 'Nota deve ser entre 1 e 5'}), 400

    comentario = data.get('comentario', '')

    set_avaliacao(avaliado, avaliador, nota, comentario)
    # avaliado.setdefault('avaliacoes', []).append({
    #     'avaliador': avaliador['nome'],
    #     'nota': nota,
    #     'comentario': comentario
    # })

    return jsonify({'mensagem': 'Avaliação registrada com sucesso'}), 201

def valida_nota(data, nota):
    if not data.get('nota'):
        return False, 'Nota é obrigatória'
    elif not isinstance(nota, int) or (nota < 1) or (nota > 5):
        return False, 'Nota deve ser entre 1 e 5'
    return True, ''

def set_avaliacao(avaliado, avaliador, nota, comentario):
    avaliado.setdefault('avaliacoes', []).append({
        'avaliador': avaliador['nome'],
        'nota': nota,
        'comentario': comentario
    })


if __name__ == '__main__':
    app.run(debug=True)
