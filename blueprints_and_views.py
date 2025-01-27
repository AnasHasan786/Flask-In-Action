from flask import Flask
from user import user_bp
from blog import blog_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(blog_bp)

@app.route('/')
def home():
    return "Welcome to My Flask App!"