from flask import Blueprint

# Create the blog blueprint
blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

from . import views

