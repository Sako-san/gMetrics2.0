from flask import Flask
from flask_cors import CORS

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Enable CORS for the app
    CORS(app)

    # Configure the database connection (if necessary)
    app.config['DATABASE'] = 'baseball-dump.db'

    # Register routes
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
