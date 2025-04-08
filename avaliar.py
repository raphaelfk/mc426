from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/avaliacao', methods=['POST'])
def avaliar():
    data = request.get_json()

    id_avaliador = data.get('id_avaliador')
    id_avaliado = data.get('id_avaliado')

    if id_avaliador is None or id_avaliado is None:
        return jsonify({'erro': 'IDs de avaliador e avaliado são obrigatórios'}), 400

    if id_avaliador == id_avaliado:
        return jsonify({'erro': 'Usuário não pode se autoavaliar'}), 400

    try:
        avaliador = usuarios[id_avaliador]
        avaliado = usuarios[id_avaliado]
    except IndexError:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    if avaliador['atividade'] != avaliado['atividade']:
        return jsonify({'erro': 'Compartilhamento da mesma rota é obrigatório'}), 400

    nota = data.get('avaliacao')
    if not isinstance(nota, int) or nota < 1 or nota > 5:
        return jsonify({'erro': 'Nota deve ser entre 1 e 5'}), 400

    comentario = data.get('comentario', '')

    avaliado['avaliacoes'].append({
        'avaliador': avaliador['nome'],
        'nota': nota,
        'comentario': comentario
    })

    return jsonify({'mensagem': 'Avaliação registrada com sucesso'}), 201

if __name__ == '__main__':
    app.run(debug=True)
