from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>I am learning about rendering templates!!</p>"


@app.route("/profile")
def profile():
    user_data = {
        "user_name": "Anas Hasan",
        "user_age": 26,
        "user_email": "anas@hasan.com",
    }

    return render_template("profile.html", **user_data)
