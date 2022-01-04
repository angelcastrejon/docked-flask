from flask import Flask

def create_app():
    """
    Create a Flask app using the app factory pattern
    :return Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # last config to load takes priority if both are present
    # loads settings from config/settings.py
    app.config.from_object('config.settings')

    # loads settings from instance folder
    # will silently fail if instance config is not available
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return Flask response
        """
        return 'Hello World!'

    return app