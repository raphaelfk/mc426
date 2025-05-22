from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    routes = db.relationship('Route', backref='user', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_point = db.Column(db.String(200), nullable=False)
    end_point = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rated_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.password_hash = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# API Routes
@app.route('/api/routes', methods=['GET'])
@login_required
def get_routes():
    routes = Route.query.filter_by(user_id=current_user.id, is_active=True).all()
    return jsonify([{
        'id': route.id,
        'start_point': route.start_point,
        'end_point': route.end_point
    } for route in routes])

@app.route('/api/routes', methods=['POST'])
@login_required
def create_route():
    data = request.get_json()
    route = Route(
        start_point=data['start_point'],
        end_point=data['end_point'],
        user_id=current_user.id
    )
    db.session.add(route)
    db.session.commit()
    return jsonify({
        'id': route.id,
        'start_point': route.start_point,
        'end_point': route.end_point
    })

@app.route('/api/routes/<int:route_id>', methods=['DELETE'])
@login_required
def delete_route(route_id):
    route = Route.query.get_or_404(route_id)
    if route.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    route.is_active = False
    db.session.commit()
    return jsonify({'message': 'Route deleted'})

@app.route('/api/matches', methods=['GET'])
@login_required
def get_matches():
    # Get all active routes except current user's
    other_routes = Route.query.filter(
        Route.user_id != current_user.id,
        Route.is_active == True
    ).all()
    
    matches = []
    for route in other_routes:
        user = User.query.get(route.user_id)
        matches.append({
            'user_id': user.id,
            'username': user.username,
            'start_point': route.start_point,
            'end_point': route.end_point
        })
    
    return jsonify(matches)

@app.route('/api/ratings', methods=['POST'])
@login_required
def create_rating():
    data = request.get_json()
    rating = Rating(
        rating=data['rating'],
        comment=data.get('comment', ''),
        user_id=current_user.id,
        rated_user_id=data['rated_user_id']
    )
    db.session.add(rating)
    db.session.commit()
    return jsonify({'message': 'Rating created'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 