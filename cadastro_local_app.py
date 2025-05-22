from flask import Flask, request, jsonify
from validators.location_validator         import validar_local_data
from utils.safety_score_calculator         import calcular_nota_seguranca
from models.location_model                 import build_local
from repositories.location_repository      import LocationRepository

app = Flask(__name__)
repo = LocationRepository()

locais = []  # Armazenamento temporário para os locais

def validar_endereco(endereco):
    return isinstance(endereco, str) and len(endereco.strip()) >= 5

def calcular_nota_seguranca(num_incidentes, relatos):
    nota = 10 - (num_incidentes * 1) - (len(relatos) * 0.5)
    return max(nota, 0)  # Garante que a nota não seja menor que 0

@app.route('/cadastrar_local', methods=['POST'])
def cadastrar_local():
    data = request.get_json()

    # 1) validação
    erros = validar_local_data(data)
    if erros:
        return jsonify({'erro': '; '.join(erros)}), 400

    # 2) cálculo da nota
    nota = calcular_nota_seguranca(
        data['numero_incidentes'],
        data['relatos']
    )

    # 3) montagem
    local = build_local(data, nota)

    # 4) persistência
    repo.add(local)

    return jsonify({'mensagem': 'Local cadastrado com sucesso!', 'local': local}), 201

