// document.getElementById('login-form').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevent form submission

//     // Retrieve form data
//     const username = document.getElementById('username').value;
//     const password = document.getElementById('password').value;

//     // Perform client-side validation
//     // You can add more validation rules here

//     // Send AJAX request to server for login
//     sendLoginData(username, password);
// });

// function sendLoginData(username, password) {
//     fetch('/login', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//             username: username,
//             password: password
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Display login result message to user
//         const messageDiv = document.getElementById('message');
//         messageDiv.textContent = data.message;
//         if (data.status === 'success') {
//             messageDiv.style.color = 'green';
//             // Redirect user to dashboard or home page
//             window.location.href = '/dashboard';
//         } else {
//             messageDiv.style.color = 'red';
//         }
//     })
//     .catch(error => console.error('Error:', error));
// }

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = data.message;
        if (data.status === 'success') {
            messageDiv.style.color = 'green';
            window.location.href = '/';
        } else {
            messageDiv.style.color = 'red';
        }
    })
    .catch(error => console.error('Error:', error));
});
