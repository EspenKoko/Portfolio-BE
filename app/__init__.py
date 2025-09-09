from flask import Flask
from flasgger import Swagger
from .extensions import db, ma
from .routes import register_routes

"""
Author          : Espen Koko
Create Date     : 09-09-2025
File            : __init__.py
"""

def create_app():
    app = Flask(__name__)
    
    template = {
    "swagger": "3.0",
    "info": {
      "title": "Flask CV API",
      "description": "This API was developed using Python Flask, which provides an interface for producing and consuming messages with Apache Kafka topics via HTTP endpoints.",
      "version": "1.0"
    }
    }
    app.config['SWAGGER'] = {
        'title': 'Flask CV API',
        'uiversion': 2,
        # 'template': './resources/flasgger/swagger_ui.html'
    }
    Swagger(app, template=template)

    app.config.from_object("config.Config")

    # Init extensions ????????
    db.init_app(app)
    ma.init_app(app)

    register_routes(app)

    return app
