from ..extensions import ma
from ..models.experience import Experience

class ExperienceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Experience
        load_instance = True

    experience_id = ma.auto_field()
    user_id = ma.auto_field()
    job_title = ma.auto_field()
    company_name = ma.auto_field()
    location = ma.auto_field()
    start_date = ma.auto_field()
    end_date = ma.auto_field()
    description = ma.auto_field()