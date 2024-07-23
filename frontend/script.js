document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('register-form');
    const messageDiv = document.getElementById('message');

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(registerForm);
            const data = {
                username: formData.get('username'),
                email: formData.get('email'),
                password: formData.get('password'),
            };

            try {
                const response = await fetch('http://localhost:5000/api/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (response.ok) {
                    const result = await response.json();
                    if (messageDiv) { // Check if messageDiv exists
                        messageDiv.textContent = result.message;
                    }
                    if (response.status === 201) {
                        window.location.href = '/thank-you.html';
                    }
                } else {
                    const errorResult = await response.json();
                    if (messageDiv) { // Check if messageDiv exists
                        messageDiv.textContent = errorResult.message || 'An error occurred during registration';
                    }
                }
            } catch (error) {
                console.error('Error:', error);
                if (messageDiv) { // Check if messageDiv exists
                    messageDiv.textContent = 'Failed to connect to the server. Please try again later.';
                }
            }
        });
    }
});
