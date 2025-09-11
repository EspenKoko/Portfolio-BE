from flask import Flask
from docs.swagger import swagger_config
from app.extensions import db, ma
from app.routes import register_routes
from app.utils.error_handlers import error_handlers

def create_app():
    app = Flask(__name__)
    
    swagger_config(app)

    app.config.from_object("app.config.Config")

    # TODO Init extensions ????
    db.init_app(app)
    ma.init_app(app)

    register_routes(app)
    error_handlers(app)
    
    return app
