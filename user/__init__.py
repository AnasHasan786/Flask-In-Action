from flask import Blueprint

# Create the user blueprint
user_bp = Blueprint('user', __name__, url_prefix='/user')

from . import views

