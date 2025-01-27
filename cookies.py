from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Hi, I am learning about the cookies!!</p>"

# Route to set a cookie
@app.route('/setcookie')
def set_cookie():
    response = make_response("Cookie has been set!")  # Create a response object
    response.set_cookie('username', 'Anas', max_age=60*60*24)  # Cookie valid for 1 day
    return response

# Route to get a cookie
@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username') # Read the cookie
    
    if username:
        return f"Welcome back, {username}!"
    else:
        return "No cookie found!"

# Route to delete a cookie
@app.route('/deletecookie')
def delete_cookie():
    response = make_response("Cookie has been deleted!")  # Create a response object
    response.set_cookie('username', '', max_age=0)  # Set cookie expiration to 0
    return response

    