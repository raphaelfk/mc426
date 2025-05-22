from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    atividade = db.Column(db.String(20), nullable=False, default='caminhada')  # caminhada, pedalada, ambos
    routes = db.relationship('Route', backref='user', lazy=True)
    ratings_given = db.relationship('Rating', 
                                  foreign_keys='Rating.user_id',
                                  backref='rater',
                                  lazy=True)
    ratings_received = db.relationship('Rating',
                                     foreign_keys='Rating.rated_user_id',
                                     backref='rated_user',
                                     lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rated_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_avaliador = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_avaliado = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text)
    tipo_avaliacao = db.Column(db.String(20), nullable=False)  # comportamento, seguranca, pontualidade 