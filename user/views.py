from flask import request, jsonify
from . import user_bp

@user_bp.route('/profile')
def profile():
    return "Welcome to the User Profile Page"

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return jsonify({"message": "Login Successful!"})
    
    return "Login Page"


