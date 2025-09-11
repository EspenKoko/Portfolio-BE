from flask import Blueprint, request, jsonify
from app.schemas.skill_schema import SkillSchema
from app.models.skill import Skill

skills_bp = Blueprint("skills", __name__)
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)

@skills_bp.route("/", methods=["GET"])
def get_skills():
    skills = Skill.query.all()
    return skills_schema.jsonify(skills)

@skills_bp.route("/<int:id>", methods=["GET"])
def get_skill(id):
    skills = Skill.query.get_or_404(id)
    print(skills_schema.jsonify(skills))
    return skills_schema.jsonify(skills)