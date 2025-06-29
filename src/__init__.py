from flask import Flask
from src.main_input import bp as main_input_bp
from src.S3_output import bp as S3_output_py

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_input_bp)
    app.register_blueprint(S3_output_py)
    return app