from ..extensions import ma
from ..models.contact_message import ContactMessage

class ContactMessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ContactMessage
        load_instance = True

    message_id = ma.auto_field()
    user_id = ma.auto_field()
    sender_name = ma.auto_field()
    sender_email = ma.auto_field()
    subject = ma.auto_field()
    message = ma.auto_field()
    sent_date = ma.auto_field()