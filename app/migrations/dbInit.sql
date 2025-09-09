CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(50),
    location VARCHAR(150),
    summary TEXT,
    profile_picture VARCHAR(255),
    linkedin_link VARCHAR(255),
    github_link VARCHAR(255)
);

CREATE TABLE education (
    education_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    institution_name VARCHAR(200) NOT NULL,
    degree VARCHAR(150),
    field_of_study VARCHAR(150),
    start_date DATE,
    end_date DATE,
    description TEXT,
    CONSTRAINT fk_education_user FOREIGN KEY (user_id) 
        REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE experience (
    experience_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    job_title VARCHAR(150) NOT NULL,
    company_name VARCHAR(200) NOT NULL,
    location VARCHAR(150),
    start_date DATE,
    end_date DATE,
    description TEXT,
    CONSTRAINT fk_experience_user FOREIGN KEY (user_id) 
        REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE skills (
    skill_id SERIAL PRIMARY KEY,
    skill_name VARCHAR(100) NOT NULL,
    proficiency_level VARCHAR(50) -- Beginner / Intermediate / Expert
);

-- junction for Many-to-Many relationship between users and skills
CREATE TABLE user_skills (
    user_skill_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    skill_id INT NOT NULL,
    CONSTRAINT fk_user_skills_user FOREIGN KEY (user_id) 
        REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_user_skills_skill FOREIGN KEY (skill_id) 
        REFERENCES skills(skill_id) ON DELETE CASCADE
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    link VARCHAR(255),
    start_date DATE,
    end_date DATE,
    CONSTRAINT fk_projects_user FOREIGN KEY (user_id) 
        REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE technologies (
    technology_id SERIAL PRIMARY KEY,
    technology VARCHAR(255)
);

CREATE TABLE project_technologies (
    project_technology_id SERIAL PRIMARY KEY,
    project_id INT NOT NULL,
    technology_id INT NOT NULL,
    CONSTRAINT fk_project_technologies_project FOREIGN KEY (project_id) 
        REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT fk_project_technologies_technology FOREIGN KEY (technology_id) 
        REFERENCES technologies(technology_id) ON DELETE CASCADE
);

CREATE TABLE certificates (
    certificate_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    issuer VARCHAR(200),
    date_issued DATE,
    expiration_date DATE,
    credential_link VARCHAR(255),
    CONSTRAINT fk_certificates_user FOREIGN KEY (user_id) 
        REFERENCES users(user_id) ON DELETE CASCADE
);

-- CONTACT MESSAGES (from visitors)
CREATE TABLE contact_messages (
    message_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    sender_name VARCHAR(150) NOT NULL,
    sender_email VARCHAR(150) NOT NULL,
    subject VARCHAR(200),
    message TEXT NOT NULL,
    sent_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_contact_user FOREIGN KEY (user_id) 
        REFERENCES users(user_id) ON DELETE CASCADE
);
