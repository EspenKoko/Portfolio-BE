from app.extensions import ma
from app.models.project import Project

class ProjectSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Project
        load_instance = True

    project_id = ma.auto_field()
    user_id = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
    link = ma.auto_field()
    start_date = ma.auto_field()
    end_date = ma.auto_field()