from flask import Blueprint, request, jsonify
from ..schemas.project_technology_schema import ProjectTechnologySchema
from ..models.project_technology import ProjectTechnology

project_technology_bp = Blueprint("project_technology", __name__)
project_technology_schema = ProjectTechnologySchema()
project_technologies_schema = ProjectTechnologySchema(many=True)  

@project_technology_bp.route("/", methods=["GET"])
def get_project_technologies():
    project_technologies = ProjectTechnology.query.all()
    return project_technologies_schema.jsonify(project_technologies)

@project_technology_bp.route("/<int:id>", methods=["GET"])
def get_project_technology(id):
    project_technology = ProjectTechnology.query.get_or_404(id)
    return project_technology_schema.jsonify(project_technology)