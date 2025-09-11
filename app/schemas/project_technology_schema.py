from app.extensions import ma
from app.models.project_technology import ProjectTechnology

class ProjectTechnologySchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProjectTechnology
        load_instance = True

    project_technology_id = ma.auto_field()
    project_id = ma.auto_field()
    technology_id = ma.auto_field()