from flask import Flask
from flasgger import Swagger

def swagger_config(app: Flask):
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
    