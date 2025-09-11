from app.extensions import db

class Technology(db.Model):
    __tablename__ = "technologies"
    
    technology_id = db.Column(db.Integer, primary_key=True)
    technology = db.Column(db.String(255), nullable=False)