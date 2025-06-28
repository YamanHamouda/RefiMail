from flask import Flask
from main_input import bp as main_input_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_input_bp)
    return app
