from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from mydb import Database
import bcrypt

user_auth_bp = Blueprint('user_auth', __name__)
db = Database(db='myexpense.db')

# @user_auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         data = request.json
#         username = data['username']
#         email = data['email']
#         password = data['password']

#         if db.user_exists(username):
#             return jsonify({'status': 'error', 'message': 'Username already exists'})

#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#         db.add_user(username, email, hashed_password)
#         return jsonify({'status': 'success', 'message': 'User registered successfully'})

#     return render_template('register.html')

@user_auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        if db.user_exists(username, email):
            return jsonify({'status': 'error', 'message': 'Username or email already exists'})

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db.add_user(username, email, hashed_password)
        return jsonify({'status': 'success', 'message': 'User registered successfully'})

    return render_template('register.html')

@user_auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        password = data['password']

        user = db.authenticate_user(username, password)
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['username']
            return jsonify({'status': 'success', 'message': 'Login successful'})

        return jsonify({'status': 'error', 'message': 'Invalid credentials'})

    return render_template('login.html')

@user_auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))
