from flask import Blueprint, request, jsonify
from flask_cors import CORS
from src.helpers.S3_input import send_email  

bp = Blueprint('main_input', __name__)
CORS(bp)

@bp.route('/api/main-input', methods=['POST'])
def handle_submit():
    data = request.json
    email = data.get('email')
    send_email(email)
    print("email sent succcessfully")
    return jsonify({"status": "success"})
