from ..extensions import db

class ProjectTechnology(db.Model):
    __tablename__ = "project_technologies"
    
    project_technology_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    technology_id = db.Column(db.Integer, db.ForeignKey("technologies.technology_id"), nullable=False)
    # project = db.relationship("Project", back_populates="technologies")
    # technology = db.relationship("Technology", back_populates="projects")