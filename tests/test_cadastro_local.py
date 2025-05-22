from app import create_app
import pytest
from app.models.local import Local
from app import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_cadastro_sucesso(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta'
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['mensagem'] == 'Local cadastrado com sucesso!'
    assert Local.query.filter_by(nome='Bolsão da BC').first() is not None

def test_todos_os_campos_vazios(client):
    resposta = client.post('/cadastrar_local', json={})
    assert resposta.status_code == 400
    assert 'Nome' in resposta.get_json()['erro']

def test_nome_invalido(client):
    resposta = client.post('/cadastrar_local', json={
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta'
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 400
    assert 'Nome' in resposta.get_json()['erro']

def test_endereco_invalido(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 12,
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 400
    assert 'Endereço inválido' == resposta.get_json()['erro']

def test_proximidade_invalida(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 400
    assert 'Proximidade' in resposta.get_json()['erro']

def test_numero_incidentes_invalido(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': -1,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 400
    assert 'Número de incidentes deve ser um número inteiro >= 0' in resposta.get_json()['erro']

def test_relatos_invalido(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': 'roubo de bicicleta',
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 400
    assert 'Relatos devem ser enviados como uma lista' in resposta.get_json()['erro']

def test_coordenadas_invalidas(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
            'capivaras atacando alunos'
        ],
        'coordenadas': {
            'latitude': 'invalido',
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 400
    assert 'Coordenadas inválidas' in resposta.get_json()['erro']

def test_tipo_local_invalido(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'invalido'
    })
    assert resposta.status_code == 400
    assert 'Tipo de local inválido' in resposta.get_json()['erro']

def test_nota_seguranca(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 2,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 201
    local = Local.query.filter_by(nome='Bolsão da BC').first()
    assert local.nota_seguranca == 8.0

def test_nota_seguranca_zero(client):
    resposta = client.post('/cadastrar_local', json={
        'nome': 'Bolsão da BC',
        'endereco': 'R. Sérgio Buarque de Holanda, 421',
        'proximidade': 'Biblioteca Central da Unicamp',
        'numero_incidentes': 10,
        'relatos': [
            'roubo de bicicleta',
            'assalto a mão armada',
        ],
        'coordenadas': {
            'latitude': -22.8175,
            'longitude': -47.0647
        },
        'tipo_local': 'estacionamento'
    })
    assert resposta.status_code == 201
    local = Local.query.filter_by(nome='Bolsão da BC').first()
    assert local.nota_seguranca == 0.0