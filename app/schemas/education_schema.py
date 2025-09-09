from ..extensions import ma
from ..models.education import Education

class EducationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Education
        load_instance = True

    education_id = ma.auto_field()
    user_id = ma.auto_field()
    institution_name = ma.auto_field()
    degree = ma.auto_field()
    field_of_study = ma.auto_field()
    start_date = ma.auto_field()
    end_date = ma.auto_field()
    description = ma.auto_field()