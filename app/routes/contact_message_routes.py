from flask import Blueprint, request, jsonify
from ..schemas.contact_message_schema import ContactMessageSchema
from ..models.contact_message import ContactMessage

contact_messages_bp = Blueprint("contact_messages", __name__)
contact_message_schema = ContactMessageSchema()
contact_messages_schema = ContactMessageSchema(many=True)

@contact_messages_bp.route("/", methods=["GET"])
def get_contact_messages():
    contact_messages = ContactMessage.query.all()
    return contact_messages_schema.jsonify(contact_messages)

@contact_messages_bp.route("/<int:id>", methods=["GET"])
def get_contact_message(id):
    contact_message = ContactMessage.query.get_or_404(id)
    return contact_message_schema.jsonify(contact_message)
