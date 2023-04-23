from app import db

class Data(db.Model):
    __tablename__ = 'measurements'

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    age = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    waist = db.Column(db.Float, nullable=False)