def calcular_nota_seguranca(num_incidentes, relatos):
    nota = 10 - (num_incidentes * 1) - (len(relatos) * 0.5)
    return max(nota, 0)
