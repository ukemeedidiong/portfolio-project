from flask import Blueprint, request, jsonify, redirect, url_for, flash
from mydb import Database

budget_management_bp = Blueprint('budget_management', __name__)
db = Database(db='myexpense.db')

# @budget_management_bp.route('/set_budget', methods=['POST'])
# def set_budget():
#     budget = float(request.form['budget'])
#     db.saveBudget(budget)  # Save or update budget in the database
#     total_expense_row = db.fetchRecord('SELECT SUM(item_price) FROM expense_record')[0]
#     total_expense = total_expense_row[0] if total_expense_row[0] is not None else 0
#     balance_remaining = budget - total_expense
#     return jsonify({'status': 'success', 'message': f'Monthly budget set to {budget}.', 'total_expense': total_expense, 'balance_remaining': balance_remaining})

@budget_management_bp.route('/set_budget', methods=['POST'])
def set_budget():
    try:
        budget = request.form['budget']
        db.saveBudget(budget)
        flash('Budget set successfully.')
    except Exception as e:
        flash(f'An error occurred: {e}')

    return redirect(url_for('index'))
# def set_budget():
#     try:
#         budget = float(request.form['budget'])
#     except ValueError:
#         return jsonify({'status': 'error', 'message': 'Invalid budget amount. Please enter a valid number.'})

#     db.saveBudget(budget)  # Save or update budget in the database
#     total_expense_row = db.fetchRecord('SELECT SUM(item_price) FROM expense_record')[0]
#     total_expense = total_expense_row[0] if total_expense_row[0] is not None else 0
#     balance_remaining = budget - total_expense

#     return jsonify({'status': 'success', 'message': f'Monthly budget set to {budget}.', 'total_expense': total_expense, 'balance_remaining': balance_remaining})
