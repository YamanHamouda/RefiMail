from flask import Flask, request, jsonify
from flask_cors import CORS
from S3_input import send_email
app = Flask(__name__)
CORS(app)

@app.route('/api/home',methods=['POST'])
def handle_submit():
    data = request.json
    email = data.get('email')
    print("Recieved email: ", email)
    send_email(email)
    return jsonify({"new_email" : email + "\n Thank you."})\

if __name__ == "__main__":
    app.run(debug=True)