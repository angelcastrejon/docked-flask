from flask import Flask

def create_app():
    """
    Create a Flask app using the app factory pattern
    TODO: add app.config from object and pyfile
    :return Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return Flask response
        """
        return 'Hello World!'

    return app