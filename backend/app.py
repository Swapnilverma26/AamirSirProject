from flask import Flask
from config import Config
from models import mongo
from routes import main
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

mongo.init_app(app)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
