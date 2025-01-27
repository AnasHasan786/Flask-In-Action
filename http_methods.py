from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return fill_login_form()
    else:
        return show_login_form()
