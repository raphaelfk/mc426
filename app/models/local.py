from app import db

class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    proximidade = db.Column(db.String(100), nullable=False)
    numero_incidentes = db.Column(db.Integer, default=0)
    relatos = db.Column(db.JSON)
    coordenadas = db.Column(db.JSON)
    tipo_local = db.Column(db.String(50), nullable=False)
    nota_seguranca = db.Column(db.Float, default=10.0)

    def __repr__(self):
        return f'<Local {self.nome}>' 