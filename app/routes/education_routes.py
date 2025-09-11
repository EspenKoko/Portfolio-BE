from flask import Blueprint, request, jsonify
from app.schemas.education_schema import EducationSchema
from app.models.education import Education

education_bp = Blueprint("education", __name__)
education_schema = EducationSchema()
educations_schema = EducationSchema(many=True)

@education_bp.route("/", methods=["GET"])
def get_educations():
    educations = Education.query.all()
    return educations_schema.jsonify(educations)

@education_bp.route("/<int:id>", methods=["GET"])
def get_education(id):
    education = Education.query.get_or_404(id)
    return education_schema.jsonify(education)
