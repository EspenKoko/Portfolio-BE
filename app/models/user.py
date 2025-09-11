from app.extensions import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(50))
    location = db.Column(db.String(150))
    summary = db.Column(db.Text)
    profile_picture = db.Column(db.String(250))
    linkedin_link = db.Column(db.String(150))
    github_link = db.Column(db.String(150))