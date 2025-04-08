from flask import Flask, request, jsonify
import re

app = Flask(__name__)

locais = []  # Armazenamento temporário para os locais

def validar_endereco(endereco):
    return isinstance(endereco, str) and len(endereco.strip()) >= 5

def calcular_nota_seguranca(num_incidentes, relatos):
    nota = 10 - (num_incidentes * 1) - (len(relatos) * 0.5)
    return max(nota, 0)  # Garante que a nota não seja menor que 0

@app.route('/cadastrar_local', methods=['POST'])
def cadastrar_local():
    data = request.get_json()

    # Validações básicas
    if not data.get('nome'):
        return jsonify({'erro': 'Nome do local é obrigatório'}), 400
    if not data.get('endereco') or not validar_endereco(data['endereco']):
        return jsonify({'erro': 'Endereço inválido'}), 400
    if not data.get('proximidade'):
        return jsonify({'erro': 'Proximidade é obrigatória'}), 400
    if not isinstance(data.get('numero_incidentes'), int) or data['numero_incidentes'] < 0:
        return jsonify({'erro': 'Número de incidentes deve ser um número inteiro >= 0'}), 400
    if not isinstance(data.get('relatos'), list):
        return jsonify({'erro': 'Relatos devem ser enviados como uma lista'}), 400

    nota_seguranca = calcular_nota_seguranca(data['numero_incidentes'], data['relatos'])

    local = {
        'nome': data['nome'],
        'endereco': data['endereco'],
        'proximidade': data['proximidade'],
        'numero_incidentes': data['numero_incidentes'],
        'relatos': data['relatos'],
        'nota_seguranca': nota_seguranca
    }

    locais.append(local)

    return jsonify({'mensagem': 'Local cadastrado com sucesso!', 'local': local}), 201
