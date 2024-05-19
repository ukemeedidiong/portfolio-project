// document.getElementById('register-form').addEventListener('submit', function(event) {
//     event.preventDefault();

//     const username = document.getElementById('username').value;
//     const email = document.getElementById('email').value;
//     const password = document.getElementById('password').value;

//     fetch('/register', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ username, email, password })
//     })
//     .then(response => response.json())
//     .then(data => {
//         const messageDiv = document.getElementById('message');
//         messageDiv.textContent = data.message;
//         if (data.status === 'success') {
//             messageDiv.style.color = 'green';
//             window.location.href = '/login';
//         } else {
//             messageDiv.style.color = 'red';
//         }
//     })
//     .catch(error => console.error('Error:', error));
// });
document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email, password })
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = data.message;
        if (data.status === 'success') {
            messageDiv.style.color = 'green';
            window.location.href = '/login';
        } else {
            messageDiv.style.color = 'red';
        }
    })
    .catch(error => console.error('Error:', error));
});
