document.addEventListener('DOMContentLoaded', function() {
    // Get form elements and buttons
    const recordForm = document.getElementById('record-form');
    const budgetForm = document.getElementById('budget-form');
    const curDateButton = document.getElementById('cur-date');
    const selectedRowIdInput = document.getElementById('selected_rowid');
    const submitBtn = document.getElementById('submit-btn');
    const updateBtn = document.createElement('button');
    const deleteBtn = document.createElement('button');
    const recordRows = document.querySelectorAll('.record-row');

    // Create update and delete buttons dynamically
    updateBtn.id = 'update-btn';
    updateBtn.textContent = 'Update Record';
    updateBtn.style.display = 'none';

    deleteBtn.id = 'delete-btn';
    deleteBtn.textContent = 'Delete Record';
    deleteBtn.style.display = 'none';

    recordForm.appendChild(updateBtn);
    recordForm.appendChild(deleteBtn);

    // Event listener for current date button
    curDateButton.addEventListener('click', function() {
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('transaction_date').value = today;
    });

    // Event listener for clicking on record rows
    recordRows.forEach(row => {
        row.addEventListener('click', function() {
            // Get data from the clicked row
            const rowid = this.dataset.rowid;
            const itemName = this.children[1].textContent;
            const itemPrice = this.children[2].textContent;
            const purchaseDate = this.children[3].textContent;

            // Populate form fields with row data
            document.getElementById('item_name').value = itemName;
            document.getElementById('item_amt').value = itemPrice;
            document.getElementById('transaction_date').value = purchaseDate;
            selectedRowIdInput.value = rowid;

            // Hide submit button, show update and delete buttons
            submitBtn.style.display = 'none';
            updateBtn.style.display = 'inline';
            deleteBtn.style.display = 'inline';
        });
    });

    // Event listener for update button click
    updateBtn.addEventListener('click', function() {
        recordForm.action = '/update_record';
        recordForm.submit();
    });

    // Event listener for delete button click
    deleteBtn.addEventListener('click', function() {
        recordForm.action = '/delete_record';
        recordForm.submit();
    });

    // Set default action for saving a new record
    recordForm.addEventListener('submit', function(event) {
        if (!selectedRowIdInput.value) {
            recordForm.action = '/save_record';
        } else {
            event.preventDefault(); // Prevent default submission if rowid is set (update/delete actions will handle it)
        }
    });

    // Handle budget form submission
    budgetForm.addEventListener('submit', function() {
        budgetForm.action = '/set_budget';
    });
});
