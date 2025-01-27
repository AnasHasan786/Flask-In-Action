from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) 
    
    def __repr__(self):
        return f"<User {self.username}>"

# Initialize Tables on App Startup
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "I am learning about Databases in Flask!"

@app.route("/create_user")
def create_user():
    new_user = User(username="Anas", email="anas@example.com", password="mypassword")
    db.session.add(new_user)
    db.session.commit()
    return "User created!"

@app.route("/view_users", methods=["GET"])
def view_users():
    with app.app_context():
        # Fetching all users
        users = User.query.all()
        
        return render_template("view_users.html", users=users)
