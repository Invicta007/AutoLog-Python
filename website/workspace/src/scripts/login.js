document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Simple validation
        if (username === '' || password === '') {
            alert('Please fill in both fields.');
            return;
        }

        // Handle form submission (e.g., send data to server)
        console.log('Username:', username);
        console.log('Password:', password);

        // Here you can add your AJAX request or fetch call to submit the form
    });
});