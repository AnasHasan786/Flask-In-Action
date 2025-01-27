from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>This is index page</p>"


@app.route("/login")
def login():
    return "<p>This is login page</p>"


@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="Tony Stark"))
