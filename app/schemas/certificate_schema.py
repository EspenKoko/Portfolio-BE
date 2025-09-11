from app.extensions import ma
from app.models.certificate import Certificate

class CertificateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Certificate
        load_instance = True

    certificate_id = ma.auto_field()
    user_id = ma.auto_field()
    title = ma.auto_field()
    issuer = ma.auto_field()
    date_issued = ma.auto_field()
    expiration_date = ma.auto_field()
    credential_link = ma.auto_field()