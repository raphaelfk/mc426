from app import create_app
import pytest
from app.models.user import User
from app.models.route import Route
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

def test_register_success(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert User.query.filter_by(username='testuser').first() is not None

def test_register_duplicate_username(client):
    # First registration
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test1@example.com',
        'password': 'password123',
        'atividade': 'caminhada'
    })

    # Try to register with same username
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test2@example.com',
        'password': 'password123',
        'atividade': 'caminhada'
    }, follow_redirects=True)
    
    assert b'Username already exists' in response.data

def test_login_success(client):
    # Register a user first
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    
    # Try to login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_login_invalid_credentials(client):
    response = client.post('/login', data={
        'username': 'nonexistent',
        'password': 'wrongpass'
    })
    assert b'Invalid username or password' in response.data

def test_create_route(client):
    # Register and login a user first
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    
    # Create a route
    response = client.post('/api/routes', json={
        'start_point': 'Point A',
        'end_point': 'Point B'
    })
    assert response.status_code == 200
    assert response.get_json()['start_point'] == 'Point A'
    assert response.get_json()['end_point'] == 'Point B'

def test_create_local(client):
    response = client.post('/cadastrar_local', json={
        'nome': 'Test Location',
        'endereco': '123 Test St',
        'proximidade': 'near',
        'numero_incidentes': 0,
        'relatos': [],
        'coordenadas': {
            'latitude': -23.5505,
            'longitude': -46.6333
        },
        'tipo_local': 'parque'
    })
    assert response.status_code == 201
    assert Local.query.filter_by(nome='Test Location').first() is not None

def test_create_rating(client):
    # Create two users
    client.post('/register', data={
        'username': 'user1',
        'email': 'user1@example.com',
        'password': 'password123'
    })
    client.post('/register', data={
        'username': 'user2',
        'email': 'user2@example.com',
        'password': 'password123'
    })
    
    # Login as user1
    client.post('/login', data={
        'username': 'user1',
        'password': 'password123'
    })
    
    # Create rating
    response = client.post('/avaliacao', json={
        'id_avaliador': 1,
        'id_avaliado': 2,
        'nota': 5,
        'comentario': 'Great user!',
        'tipo_avaliacao': 'comportamento'
    })
    assert response.status_code == 201
    assert response.get_json()['mensagem'] == 'Avaliação registrada com sucesso'

