from flask import Blueprint, request, jsonify
from flask_cors import CORS
from src.helpers.S3_input import send_email  
import uuid

bp = Blueprint('main_input', __name__)
CORS(bp)

@bp.route('/api/main-input', methods=['POST'])
def handle_submit():
    data = request.json
    email = data.get('email')
    id = uuid.uuid4()
    send_email(email = email, id = id)
    print("email sent succcessfully", email)
    print(f"id created: {id}")
    return jsonify({"id" : id})
