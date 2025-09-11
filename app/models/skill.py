from app.extensions import db

class Skill(db.Model):
    __tablename__ = "skills"
    
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    proficiency_level = db.Column(db.String(50))  # Beginner / Intermediate / Expert
    # users = db.relationship("User", secondary="user_skills", back_populates="skills")