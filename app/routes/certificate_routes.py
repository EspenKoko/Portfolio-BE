from flask import Blueprint, request, jsonify
from app.schemas.certificate_schema import CertificateSchema
from app.models.certificate import Certificate

certificates_bp = Blueprint("certificates", __name__)
certificate_schema = CertificateSchema()
certificates_schema = CertificateSchema(many=True)

@certificates_bp.route("/", methods=["GET"])
def get_certificates():
    certificates = Certificate.query.all()
    return certificates_schema.jsonify(certificates)

@certificates_bp.route("/<int:id>", methods=["GET"])
def get_certificate(id):
    certificate = Certificate.query.get_or_404(id)
    return certificate_schema.jsonify(certificate)
