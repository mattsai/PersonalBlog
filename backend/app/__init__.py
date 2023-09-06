from flask import Flask
from flask_cors import CORS, cross_origin
from app.routes import bp_routes

def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    cors = CORS(app)
    app.debug = True  #Hot-reload
    
    app.register_blueprint(bp_routes,url_prefix="/")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  



    return app