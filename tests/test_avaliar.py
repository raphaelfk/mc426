from app import create_app
import pytest
from app.models.user import User
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

@pytest.fixture
def setup_users(client):
    # Setup test users
    users = [
        {
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'password123',
            'atividade': 'caminhada'
        },
        {
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'password123',
            'atividade': 'caminhada'
        },
        {
            'username': 'carol',
            'email': 'carol@example.com',
            'password': 'password123',
            'atividade': 'pedalada'
        }
    ]
    # Add users to the database
    for user in users:
        client.post('/register', data=user)
    return users

def test_avaliacao_valida(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })
    
    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 2,
        'nota': 5,
        'comentario': 'Muito bom',
        'tipo_avaliacao': 'comportamento'
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['mensagem'] == 'Avaliação registrada com sucesso'

def test_sem_id_avaliador(client):
    resposta = client.post('/avaliacao', json={})
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'ID do avaliador é obrigatório'

def test_sem_id_avaliado(client):
    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'ID do avaliado é obrigatório'

def test_autoavaliacao(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })
    
    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 1,
        'nota': 4,
        'tipo_avaliacao': 'comportamento'
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Usuário não pode se autoavaliar'

def test_id_invalido(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })
    
    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 10,
        'nota': 4,
        'tipo_avaliacao': 'comportamento'
    })
    assert resposta.status_code == 404
    assert resposta.get_json()['erro'] == 'Usuário não encontrado'

def test_atividade_diferente(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })

    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 3,  # carol has different atividade
        'nota': 4,
        'tipo_avaliacao': 'comportamento'
    })
    assert resposta.status_code == 400
    assert 'Compartilhamento da mesma rota é obrigatório' in resposta.get_json()['erro']

def test_sem_nota(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })
    
    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 2,
        'tipo_avaliacao': 'comportamento'
    })
    assert resposta.status_code == 400
    assert 'Nota' in resposta.get_json()['erro']

def test_nota_invalida(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })
    
    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 2,
        'nota': 10,
        'tipo_avaliacao': 'comportamento'
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Nota deve ser entre 1 e 5'

def test_tipo_avaliacao_invalido(client, setup_users):
    # Login as first user
    client.post('/login', data={
        'username': 'alice',
        'password': 'password123'
    })

    resposta = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 2,
        'nota': 4,
        'tipo_avaliacao': 'invalido'
    })
    assert resposta.status_code == 400
    assert 'Tipo de avaliação inválido' in resposta.get_json()['erro']
