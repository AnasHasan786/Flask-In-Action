from flask import Flask, session
import secrets

app = Flask(__name__)

# Using a securely generated secret key
app.secret_key = secrets.token_hex(24)

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in!'

@app.route('/login/<username>')
def login(username):
    session["username"] = username
    return f'Logged in as {username}'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'You have been logged out!'


