from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.education import Education
from app.models.experience import Experience
from app.models.skill import Skill
from app.models.user_skill import UserSkill
from app.models.project import Project
from app.models.certificate import Certificate
from app.models.contact_message import ContactMessage
from app.models.technology import Technology
from app.models.project_technology import ProjectTechnology

def seed():
    # Users
    user1 = User(
        name="Alice Smith",
        email="alice@example.com",
        phone="1234567890",
        location="New York",
        summary="Software engineer with 5 years experience.",
        profile_picture="https://example.com/alice.jpg",
        linkedin_link="https://linkedin.com/in/alicesmith",
        github_link="https://github.com/alicesmith"
    )
    user2 = User(
        name="Bob Johnson",
        email="bob@example.com",
        phone="0987654321",
        location="San Francisco",
        summary="Data scientist and AI enthusiast.",
        profile_picture="https://example.com/bob.jpg",
        linkedin_link="https://linkedin.com/in/bobjohnson",
        github_link="https://github.com/bobjohnson"
    )
    db.session.add_all([user1, user2])
    db.session.commit()

    # Education
    edu1 = Education(
        user_id=user1.user_id,
        institution_name="MIT",
        degree="BSc Computer Science",
        field_of_study="Computer Science",
        start_date="2015-09-01",
        end_date="2019-06-01",
        description="Studied computer science."
    )
    edu2 = Education(
        user_id=user2.user_id,
        institution_name="Stanford",
        degree="MSc Data Science",
        field_of_study="Data Science",
        start_date="2016-09-01",
        end_date="2018-06-01",
        description="Studied data science."
    )
    db.session.add_all([edu1, edu2])
    db.session.commit()

    # Experience
    exp1 = Experience(
        user_id=user1.user_id,
        job_title="Backend Developer",
        company_name="TechCorp",
        location="New York",
        start_date="2019-07-01",
        end_date="2022-08-01",
        description="Developed backend services."
    )
    exp2 = Experience(
        user_id=user2.user_id,
        job_title="Data Analyst",
        company_name="DataInc",
        location="San Francisco",
        start_date="2018-07-01",
        end_date="2021-08-01",
        description="Analyzed data for business insights."
    )
    db.session.add_all([exp1, exp2])
    db.session.commit()

    # Skills
    skill1 = Skill(skill_name="Python", proficiency_level="Expert")
    skill2 = Skill(skill_name="SQL", proficiency_level="Intermediate")
    skill3 = Skill(skill_name="Machine Learning", proficiency_level="Expert")
    db.session.add_all([skill1, skill2, skill3])
    db.session.commit()

    # UserSkills
    us1 = UserSkill(user_id=user1.user_id, skill_id=skill1.skill_id)
    us2 = UserSkill(user_id=user1.user_id, skill_id=skill2.skill_id)
    us3 = UserSkill(user_id=user2.user_id, skill_id=skill3.skill_id)
    db.session.add_all([us1, us2, us3])
    db.session.commit()

    # Technologies
    tech1 = Technology(technology="Python")
    tech2 = Technology(technology="Flask")
    tech3 = Technology(technology="PostgreSQL")
    tech4 = Technology(technology="TensorFlow")
    db.session.add_all([tech1, tech2, tech3, tech4])
    db.session.commit()

    # Projects
    proj1 = Project(
        user_id=user1.user_id,
        name="CV Builder",
        description="A web app for building CVs.",
        link="https://github.com/alicesmith/cvbuilder",
        start_date="2021-01-01",
        end_date="2021-06-01"
    )
    proj2 = Project(
        user_id=user2.user_id,
        name="AI Chatbot",
        description="A chatbot using machine learning.",
        link="https://github.com/bobjohnson/aichatbot",
        start_date="2020-03-01",
        end_date="2020-09-01"
    )
    db.session.add_all([proj1, proj2])
    db.session.commit()

    # ProjectTechnologies (link projects and technologies)
    pt1 = ProjectTechnology(project_id=proj1.project_id, technology_id=tech1.technology_id)  # Python for CV Builder
    pt2 = ProjectTechnology(project_id=proj1.project_id, technology_id=tech2.technology_id)  # Flask for CV Builder
    pt3 = ProjectTechnology(project_id=proj1.project_id, technology_id=tech3.technology_id)  # PostgreSQL for CV Builder
    pt4 = ProjectTechnology(project_id=proj2.project_id, technology_id=tech1.technology_id)  # Python for AI Chatbot
    pt5 = ProjectTechnology(project_id=proj2.project_id, technology_id=tech4.technology_id)  # TensorFlow for AI Chatbot
    db.session.add_all([pt1, pt2, pt3, pt4, pt5])
    db.session.commit()

    # Certificates
    cert1 = Certificate(
        user_id=user1.user_id,
        title="AWS Certified Developer",
        issuer="Amazon",
        date_issued="2022-01-15",
        expiration_date="2025-01-15",
        credential_link="https://aws.amazon.com/cert1"
    )
    cert2 = Certificate(
        user_id=user2.user_id,
        title="TensorFlow Developer",
        issuer="Google",
        date_issued="2021-05-20",
        expiration_date="2024-05-20",
        credential_link="https://google.com/cert2"
    )
    db.session.add_all([cert1, cert2])
    db.session.commit()

    # Contact Messages
    msg1 = ContactMessage(
        user_id=user1.user_id,
        sender_name="Charlie",
        sender_email="charlie@example.com",
        subject="Job Opportunity",
        message="Are you interested in a backend developer role?",
        sent_date="2025-09-09 10:00:00"
    )
    msg2 = ContactMessage(
        user_id=user2.user_id,
        sender_name="Dana",
        sender_email="dana@example.com",
        subject="Collaboration",
        message="Would you like to collaborate on an AI project?",
        sent_date="2025-09-09 11:00:00"
    )
    db.session.add_all([msg1, msg2])
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed()
        print("Dummy data inserted.")