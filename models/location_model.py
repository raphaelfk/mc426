def build_local(data, nota_seguranca):
    return {
        'nome': data['nome'],
        'endereco': data['endereco'],
        'proximidade': data['proximidade'],
        'numero_incidentes': data['numero_incidentes'],
        'relatos': data['relatos'],
        'nota_seguranca': nota_seguranca
    }
