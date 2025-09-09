from ..extensions import db

class UserSkill(db.Model):
    __tablename__ = "user_skills"
    
    user_skill_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey("skills.skill_id"), nullable=False)
    # user = db.relationship("User", back_populates="skills")
    # skill = db.relationship("Skills", back_populates="users")