from app.extensions import db

class Certificate(db.Model):
    __tablename__ = "certificates"
    
    certificate_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    issuer = db.Column(db.String(150), nullable=False)
    date_issued = db.Column(db.Date)
    expiration_date = db.Column(db.Date)
    credential_link = db.Column(db.Text)
    # user = db.relationship("User", back_populates="certificates")