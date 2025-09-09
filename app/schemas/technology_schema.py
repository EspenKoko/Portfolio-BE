from ..extensions import ma
from ..models.technology import Technology

class TechnologySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Technology
        load_instance = True

    technology_id = ma.auto_field()
    technology = ma.auto_field()