from flask import Blueprint, request, jsonify
from app.schemas.project_schema import ProjectSchema
from app.models.project import Project

projects_bp = Blueprint("projects", __name__)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

@projects_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return projects_schema.jsonify(projects)

@projects_bp.route("/<int:id>", methods=["GET"])
def get_project(id):
    project = Project.query.get_or_404(id)
    return project_schema.jsonify(project)
