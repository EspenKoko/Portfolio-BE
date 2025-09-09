from ..extensions import db

class Education(db.Model):
    __tablename__ = "education"
    
    education_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    institution_name = db.Column(db.String(150), nullable=False)
    degree = db.Column(db.String(150), nullable=False)
    field_of_study = db.Column(db.String(150))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)
    # user = db.relationship("User", back_populates="education")
