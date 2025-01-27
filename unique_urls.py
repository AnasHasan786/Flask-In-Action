from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello Flask!!</p>"


@app.route("/about")
def about():
    return "<p>This is my about page.</p>"


@app.route("/myFiles/")
def files():
    return "<p>This page is gonna show my files.</p>"
