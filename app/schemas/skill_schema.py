from app.extensions import ma
from app.models.skill import Skill

class SkillSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Skill
        load_instance = True

    skill_id = ma.auto_field()
    skill_name = ma.auto_field()
    proficiency_level = ma.auto_field()