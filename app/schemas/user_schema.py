from ..extensions import ma
from ..models.user import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    user_id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    location = ma.auto_field()
    summary = ma.auto_field()
    profile_picture = ma.auto_field()
    linkedin_link = ma.auto_field()
    github_link = ma.auto_field()