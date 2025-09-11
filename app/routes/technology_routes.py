from flask import Blueprint, request, jsonify
from app.schemas.technology_schema import TechnologySchema
from app.models.technology import Technology

technology_bp = Blueprint("technology", __name__)
technology_schema = TechnologySchema()
technologies_schema = TechnologySchema(many=True)

@technology_bp.route("/", methods=["GET"])
def get_technologies():
    technologies = Technology.query.all()
    return technologies_schema.jsonify(technologies)

@technology_bp.route("/<int:id>", methods=["GET"])
def get_technology(id):
    technology = Technology.query.get_or_404(id)
    return technology_schema.jsonify(technology)