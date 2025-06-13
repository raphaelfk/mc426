from cadastro_local_app import app

def test_cadastro_sucesso():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['mensagem'] == 'Local cadastrado com sucesso!'


def test_todos_os_campos_vazios():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={})
    assert resposta.status_code == 400
    assert 'Nome' in resposta.get_json()['erro']


def test_nome_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 400
    assert 'Nome' in resposta.get_json()['erro']

def test_endereco_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 12,
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 400
    assert 'Endereço inválido' == resposta.get_json()['erro']

def test_proximidade_invalida():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 400
    assert 'Proximidade' in resposta.get_json()['erro']

def test_numero_incidentes_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': -1,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 400
    assert 'Número de incidentes deve ser um número inteiro >= 0' in resposta.get_json()['erro']

def test_relatos_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': 'roubo de biciclate'
    })
    assert resposta.status_code == 400
    assert 'Relatos devem ser enviados como uma lista' in resposta.get_json()['erro']

def test_nota_seguranca():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['local']['nota_seguranca'] == 7.0

def test_nota_seguranca_zero():
    cliente = app.test_client()
    resposta = cliente.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 10,
        'relatos': [
            'roubo de biciclate',
            'assalto a mão armada',
        ]
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['local']['nota_seguranca'] == 0.0
