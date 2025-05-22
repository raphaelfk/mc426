def validar_endereco(endereco):
    return isinstance(endereco, str) and len(endereco.strip()) >= 5

def validar_local_data(data):
    erros = []
    if not data.get('nome'):
        erros.append('Nome do local é obrigatório')
    if not data.get('endereco') or not validar_endereco(data['endereco']):
        erros.append('Endereço inválido')
    if not data.get('proximidade'):
        erros.append('Proximidade é obrigatória')
    if not isinstance(data.get('numero_incidentes'), int) or data['numero_incidentes'] < 0:
        erros.append('Número de incidentes deve ser um número inteiro >= 0')
    if not isinstance(data.get('relatos'), list):
        erros.append('Relatos devem ser enviados como uma lista')
    return erros
