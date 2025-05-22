from app import db

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_point = db.Column(db.String(200), nullable=False)
    end_point = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True) 