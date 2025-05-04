from app import app

def test_cadastro_sucesso():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={
        'nome': 'João Silva',
        'cpf': '12345678901',
        'email': 'joao@email.com',
        'senha': 'senha123',
        'atividade': 'caminhada'
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['mensagem'] == 'Usuário cadastrado com sucesso!'


def test_todos_os_campos_vazios():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={})
    assert resposta.status_code == 400
    assert 'Nome' in resposta.get_json()['erro']


def test_nome_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={
        'cpf': '12345678901',
        'email': 'joao@email.com',
        'senha': 'senha123',
        'atividade': 'caminhada'
    })
    assert resposta.status_code == 400
    assert 'Nome' in resposta.get_json()['erro']


def test_cadastro_email_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={
        'nome': 'Ana',
        'cpf': '12345678901',
        'email': 'email-invalido',
        'senha': 'senha123',
        'atividade': 'pedalada'
    })
    assert resposta.status_code == 400
    assert 'E-mail inválido' in resposta.get_json()['erro']

def test_cadastro_cpf_invalido():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={
        'nome': 'Carlos',
        'cpf': 'abc123',
        'email': 'carlos@email.com',
        'senha': 'senha123',
        'atividade': 'ambos'
    })
    assert resposta.status_code == 400
    assert 'CPF inválido' in resposta.get_json()['erro']

def test_cadastro_senha_curta():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={
        'nome': 'Julia',
        'cpf': '12345678901',
        'email': 'julia@email.com',
        'senha': '123',
        'atividade': 'caminhada'
    })
    assert resposta.status_code == 400
    assert 'Senha' in resposta.get_json()['erro']

def test_atividade_errada():
    cliente = app.test_client()
    resposta = cliente.post('/cadastro', json={
        'nome': 'Julia',
        'cpf': '12345678901',
        'email': 'julia@email.com',
        'senha': '123456',
        'atividade': 'natação' 
    })
    assert resposta.status_code == 400
    assert 'atividade' in resposta.get_json()['erro'].lower()

