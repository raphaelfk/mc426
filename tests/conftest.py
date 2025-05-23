import os
import sys
import pytest
from datetime import datetime, timedelta

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import app factory
from app import create_app, db

@pytest.fixture(scope='session')
def app():
    """Create and configure a Flask app for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function')
def test_user(app):
    """Create a test user."""
    from app.models.user import User
    # Clean up any existing users
    db.session.rollback()  # Rollback any pending transactions
    User.query.delete()
    db.session.commit()
    
    user = User(
        username='testuser',
        email='test@example.com',
        atividade='caminhada'
    )
    user.set_password('validpassword123')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture(scope='function')
def test_route(app, test_user):
    """Create a test route."""
    from app.models.route import Route
    db.session.rollback()  # Rollback any pending transactions
    Route.query.delete()
    db.session.commit()
    
    route = Route(
        user_id=test_user.id,
        start_point='Start Location',
        end_point='End Location',
        is_active=True
    )
    db.session.add(route)
    db.session.commit()
    return route 