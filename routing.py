from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello Flask!!</p>"


@app.route("/about")
def about():
    return "<p>I am learning in depth Flask!!</p>"
