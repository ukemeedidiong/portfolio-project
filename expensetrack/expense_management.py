from flask import Blueprint, request, jsonify, redirect, url_for, flash
from mydb import Database

expense_management_bp = Blueprint('expense_management', __name__)
db = Database(db='myexpense.db')


@expense_management_bp.route('/save_record', methods=['POST'])
def save_record():
    try:
        item_name = request.form['item_name']
        item_price = float(request.form['item_price'])  # Ensure the price is a float
        purchase_date = request.form['purchase_date']
        rowid = request.form.get('rowid')

        current_total_expense = db.fetchTotalExpense()
        budget = db.fetchBudget()

        # Calculate the new total expense after adding/updating the record
        if rowid:
            # If updating, fetch the old record to subtract its price from the current total expense
            old_record = db.fetchRecord(f"SELECT item_price FROM expense_record WHERE rowid = {rowid}")[0]
            old_price = old_record[0]
            new_total_expense = current_total_expense - old_price + item_price
        else:
            new_total_expense = current_total_expense + item_price

        # Check if the new total expense exceeds the budget
        if new_total_expense > budget:
            flash('Error: Adding this expense exceeds your budget.', 'error')
            return redirect(url_for('index'))

        if rowid:  # If rowid exists, it's an update
            db.updateRecord(item_name, item_price, purchase_date, rowid)
        else:  # Otherwise, it's a new record
            db.insertRecord(item_name, item_price, purchase_date)

        flash('Record saved successfully.')
    except Exception as e:
        flash(f'An error occurred: {e}', 'error')

    return redirect(url_for('index'))

# def save_record():
#     try:
#         item_name = request.form['item_name']
#         item_price = request.form['item_price']
#         purchase_date = request.form['purchase_date']
#         rowid = request.form.get('rowid')

#         if rowid:  # If rowid exists, it's an update
#             db.updateRecord(item_name, item_price, purchase_date, rowid)
#         else:  # Otherwise, it's a new record
#             db.insertRecord(item_name, item_price, purchase_date)

#         flash('Record saved successfully.')
#     except Exception as e:
#         flash(f'An error occurred: {e}')

#     return redirect(url_for('index'))


@expense_management_bp.route('/update_record', methods=['POST'])
def update_record():
    try:
        rowid = request.form['rowid']
        item_name = request.form['item_name']
        item_price = float(request.form['item_price'])
        purchase_date = request.form['purchase_date']
        db.updateRecord(item_name, item_price, purchase_date, rowid)
        flash('Record updated successfully.')
    except KeyError as e:
        flash(f'Missing form field: {str(e)}')
    return redirect(url_for('index'))


@expense_management_bp.route('/delete_record', methods=['POST'])
def delete_record():
    try:
        rowid = request.form['rowid']
        db.removeRecord(rowid)
        flash('Record deleted successfully.')
    except KeyError as e:
        flash(f'Missing form field: {str(e)}')
    return redirect(url_for('index'))
