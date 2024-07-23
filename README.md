# Full-Stack Web Application with Flask and MongoDB

## Setup Instructions

### Backend

1. Navigate to the `backend` directory:
    ```sh
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure MongoDB is running locally or provide a MongoDB URI in `config.py`.

5. Run the Flask app:
    ```sh
    python app.py
    ```

The backend will be running on `http://localhost:5000`.

### Frontend

1. Navigate to the `frontend` directory and open `index.html` in your browser.

### Deployment

To deploy the backend and frontend individually:

1. **Backend**: Deploy the `backend` folder to a server or a cloud service (e.g., AWS, Heroku).
2. **Frontend**: Deploy the `frontend` folder to a static site hosting service (e.g., Netlify, Vercel).

Make sure to update the API endpoints in `frontend/script.js` to match your deployed backend URL.

## Access the Application

Open your web browser and go to the deployed frontend URL. You can register a new user and log in with the registered credentials.
