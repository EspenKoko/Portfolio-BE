from flask import Blueprint, request, jsonify
from app.schemas.user_skills_schema import UserSkillsSchema
from app.models.user_skill import UserSkill

user_skills_bp = Blueprint("user_skills", __name__)
user_skills_schema = UserSkillsSchema()
user_skills_list_schema = UserSkillsSchema(many=True)

@user_skills_bp.route("/", methods=["GET"])
def get_user_skills():
    user_skills = UserSkill.query.all()
    return user_skills_list_schema.jsonify(user_skills)

@user_skills_bp.route("/<int:id>", methods=["GET"])
def get_user_skill(id):
    user_skill = UserSkill.query.get_or_404(id)
    return user_skills_schema.jsonify(user_skill)
