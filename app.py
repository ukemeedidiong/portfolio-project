# # from flask import Flask, render_template, session, redirect, url_for, request
# # from expensetrack.user_auth import user_auth_bp
# # from expensetrack.expense_management import expense_management_bp
# # from expensetrack.budget_management import budget_management_bp
# # from mydb import Database

# # app = Flask(__name__, template_folder='template')
# # app.secret_key = '#1711nyesSonsamp'

# # # Register blueprints
# # app.register_blueprint(user_auth_bp)
# # app.register_blueprint(expense_management_bp)
# # app.register_blueprint(budget_management_bp)

# # db = Database(db='myexpense.db')

# # @app.route('/')
# # def index():
# #     budget = db.get_budget()
# #     total_expense = db.fetchTotalExpense()
# #     records = db.fetchRecord("SELECT * FROM expense_record")
# #     user_name = session.get('user_name', 'Guest')
# #     return render_template('index.html', user_name=user_name, total_expense=total_expense, budget=budget, records=records)

# # @app.route('/debug')
# # def debug():
# #     records = db.fetchRecord("SELECT * FROM expense_record")
# #     return str(records)

# # @expense_management_bp.route('/save_record', methods=['POST'])
# # def save_record():
# #     item_name = request.form['item_name']
# #     item_price = float(request.form['item_price'])  # Update to match the form field name
# #     purchase_date = request.form['purchase_date']
# #     serial_no = request.form.get('rowid', '')  # Adjust if necessary

# #     db.insertRecord(serial_no, item_name, item_price, purchase_date)
# #     return redirect(url_for('index'))

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, session, redirect, url_for
# from expensetrack.user_auth import user_auth_bp
# from expensetrack.expense_management import expense_management_bp
# from expensetrack.budget_management import budget_management_bp
# from mydb import Database

# app = Flask(__name__, template_folder='template')
# app.secret_key = '#1711nyesSonsamp'
# db = Database(db='myexpense.db')

# # Register blueprints
# app.register_blueprint(user_auth_bp)
# app.register_blueprint(expense_management_bp)
# app.register_blueprint(budget_management_bp)

# # Other routes
# @app.route('/')
# def index():
#     budget = db.get_budget()  # You need to implement this function in mydb.py
#     total_expense = db.fetchTotalExpense()
#     records = db.fetchRecord("SELECT * FROM expense_record")

#     user_name = session.get('user_name', 'Guest')
#     return render_template('index.html', user_name=user_name, total_expense=total_expense, budget=budget, records=records)

# @app.route('/debug')
# def debug():
#     records = db.fetchRecord("SELECT * FROM expense_record")
#     return str(records)

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, session, redirect, url_for, request, jsonify, flash
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from expensetrack.user_auth import user_auth_bp
# from expensetrack.expense_management import expense_management_bp
# from expensetrack.budget_management import budget_management_bp
# from mydb import Database

# app = Flask(__name__, template_folder='template')
# app.secret_key = '#1711nyesSonsamp'

# # Initialize the database
# db = Database(db='myexpense.db')

# # Initialize Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# # Register blueprints
# app.register_blueprint(user_auth_bp)
# app.register_blueprint(expense_management_bp)
# app.register_blueprint(budget_management_bp)

# # User class for Flask-Login
# class User(UserMixin):
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     @staticmethod
#     def get(user_id):
#         user = db.get_user_by_id(user_id)
#         if user:
#             return User(user[0], user[1], user[2])
#         return None

#     @staticmethod
#     def find_by_username(username):
#         user = db.get_user_by_username(username)
#         if user:
#             return User(user[0], user[1], user[2])
#         return None

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# # Home route
# @app.route('/')
# @login_required
# def index():
#     budget = db.get_budget()
#     total_expense = db.fetchTotalExpense()
#     records = db.fetchRecord("SELECT * FROM expense_record")
#     user_name = current_user.username
#     return render_template('index.html', user_name=user_name, total_expense=total_expense, budget=budget, records=records)

# # Debug route
# @app.route('/debug')
# def debug():
#     records = db.fetchRecord("SELECT * FROM expense_record")
#     return str(records)

# # Login route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         data = request.get_json()
#         username = data['username']
#         password = data['password']
#         user = User.find_by_username(username)
#         if user and db.verify_password(password, user.password):
#             login_user(user)
#             return jsonify({'status': 'success', 'message': 'Logged in successfully!'})
#         return jsonify({'status': 'failure', 'message': 'Invalid username or password'})
#     return render_template('login.html')

# # Register route
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         data = request.get_json()
#         username = data['username']
#         email = data['email']
#         password = data['password']
#         existing_user = User.find_by_username(username)
#         if existing_user:
#             return jsonify({'status': 'failure', 'message': 'Username already exists'})
#         db.add_user(username, email, password)
#         return jsonify({'status': 'success', 'message': 'User registered successfully'})
#     return render_template('register.html')

# # Logout route
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, session, redirect, url_for
# from expensetrack.user_auth import user_auth_bp
# from expensetrack.expense_management import expense_management_bp
# from expensetrack.budget_management import budget_management_bp
# from mydb import Database

# app = Flask(__name__, template_folder='templates')
# app.secret_key = '#1711nyesSonsamp'
# db = Database(db='instance/myexpense.db')

# # Register blueprints
# app.register_blueprint(user_auth_bp)
# app.register_blueprint(expense_management_bp)
# app.register_blueprint(budget_management_bp)

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         return redirect(url_for('user_auth.login'))

#     budget = db.get_budget()  # You need to implement this function in mydb.py
#     total_expense = db.fetchTotalExpense()
#     records = db.fetchRecord("SELECT * FROM expense_record")

#     user_name = session.get('user_name', 'Guest')
#     return render_template('index.html', user_name=user_name, total_expense=total_expense, budget=budget, records=records)
# # def index():
# #     if 'user_name' not in session:
# #         return redirect(url_for('user_auth.login_page'))
# #     budget = db.get_budget()
# #     total_expense = db.fetchTotalExpense()
# #     records = db.fetchRecord("SELECT * FROM expense_record")

# #     user_name = session.get('user_name', 'Guest')
# #     return render_template('index.html', user_name=user_name, total_expense=total_expense, budget=budget, records=records)

# @app.route('/register')
# def register_page():
#     return render_template('register.html')

# @app.route('/login')
# def login_page():
#     return render_template('login.html')

# @app.route('/debug')
# def debug():
#     records = db.fetchRecord("SELECT * FROM expense_record")
#     return str(records)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, session, redirect, url_for
from expensetrack.user_auth import user_auth_bp
from expensetrack.expense_management import expense_management_bp
from expensetrack.budget_management import budget_management_bp
from mydb import Database

app = Flask(__name__, template_folder='template')  # Ensure template_folder is set to 'templates'
app.secret_key = '#1711nyesSonsamp'
db = Database(db='myexpense.db')

# Register blueprints
app.register_blueprint(user_auth_bp)
app.register_blueprint(expense_management_bp)
app.register_blueprint(budget_management_bp)
app.register_blueprint(user_auth_bp, url_prefix='/auth', name='user_auth_bp')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('user_auth.register'))

    budget = db.get_budget()
    total_expense = db.fetchTotalExpense()
    records = db.fetchRecord("SELECT * FROM expense_record")

    user_name = session.get('user_name', 'Guest')
    return render_template('index.html', user_name=user_name, total_expense=total_expense, budget=budget, records=records)




@app.route('/register_success')
def register_success():
    return redirect(url_for('user_auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
