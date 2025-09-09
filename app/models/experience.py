from ..extensions import db

class Experience(db.Model):
    __tablename__ = "experience"
    
    experience_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)
    # user = db.relationship("User", back_populates="experience")