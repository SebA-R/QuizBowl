from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from .api.routes import api
from .site.routes import site
from .admin.routes import admin_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api)
    app.register_blueprint(site)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app