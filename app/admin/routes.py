# admin/admin.py

from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User 
from app import db 

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
admin = Admin(template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))

admin.init_app(admin_bp)
