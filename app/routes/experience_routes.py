from flask import Blueprint, request, jsonify
from app.schemas.experience_schema import ExperienceSchema
from app.models.experience import Experience

experience_bp = Blueprint("experience", __name__)
experience_schema = ExperienceSchema()
experiences_schema = ExperienceSchema(many=True)

@experience_bp.route("/", methods=["GET"])
def get_experiences():
    experiences = Experience.query.all()
    return experiences_schema.jsonify(experiences)

@experience_bp.route("/<int:id>", methods=["GET"])
def get_experience(id):
    experience = Experience.query.get_or_404(id)
    return experience_schema.jsonify(experience)
