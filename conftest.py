# This file, placed at the project root or within a tests subdirectory,
# is where you can define fixtures that are globally available to tests in the same directory and its subdirectories

import pytest
from app import create_app
from app.extensions import db

@pytest.fixture(scope='function')
def memory_db():
	app = create_app()
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	with app.app_context():
		db.create_all()
		yield db
		db.session.remove()
		db.drop_all()