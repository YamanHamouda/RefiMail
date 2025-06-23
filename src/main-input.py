from flask import Flask, request,jsonify, make_response
from flask_cors import CORS
from S3_input import send_email

app = Flask(__name__)
CORS(app) 


@app.route('/api/main-input',methods=['POST'])
def handle_submit():
    print("getting email")
    data = request.json
    email = data.get('email')
    print("Recieved the email: ", email)
    send_email(email)
    print("email sent")
    return jsonify({"status" : "success"})

if __name__ == "__main__":
    app.run(debug=True)