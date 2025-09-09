from .user_routes import user_bp
from .actuater_routes import actuater_bp
from .skill_routes import skills_bp
from .user_skills_routes import user_skills_bp
from .experience_routes import experience_bp
from .education_routes import education_bp
from .project_routes import projects_bp
from .certificate_routes import certificates_bp
from .contact_message_routes import contact_messages_bp
from .technology_routes import technology_bp
from .project_technology_routes import project_technology_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(actuater_bp, url_prefix="/api/actuater")
    app.register_blueprint(skills_bp, url_prefix="/api/skills")
    app.register_blueprint(user_skills_bp, url_prefix="/api/user_skills")
    app.register_blueprint(experience_bp, url_prefix="/api/experience")
    app.register_blueprint(education_bp, url_prefix="/api/education")
    app.register_blueprint(projects_bp, url_prefix="/api/projects")
    app.register_blueprint(certificates_bp, url_prefix="/api/certificates")
    app.register_blueprint(contact_messages_bp, url_prefix="/api/contact_messages")
    app.register_blueprint(technology_bp, url_prefix="/api/technologies")
    app.register_blueprint(project_technology_bp, url_prefix="/api/project_technologies")
