from app.extensions import ma
from app.models.user_skill import UserSkill

class UserSkillsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserSkill
        load_instance = True

    user_id = ma.auto_field()
    skill_id = ma.auto_field()