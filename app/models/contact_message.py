from ..extensions import db

class ContactMessage(db.Model):
    __tablename__ = "contact_messages"
    
    message_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    sender_name = db.Column(db.String(150), nullable=False)
    sender_email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    sent_date = db.Column(db.DateTime, server_default=db.func.now())