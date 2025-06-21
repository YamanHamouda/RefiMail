import boto3
from botocore.exceptions import ClientError

from flask_cors import CORS
from flask import Flask, request
import time

print(__name__)
app = Flask(__name__)
CORS(app)

@app.route("/api/output", methods=["POST"])
def get_refined_email():
   email = get_email()
   print(email)
    


def get_email():
    while(True):
        time.sleep(100)
        try:
            s3 = boto3.client("s3")
            bucket = "yaman-hamouda-aws-lambda-hackathon-output"
            key = "output_email.txt"

            s3_object = s3.get_object(Bucket=bucket, Key=key)
            file = s3_object['Body']
            new_email = file.read().decode('utf-8')
            return new_email
        except ClientError as e:
            if e.responsep['Error']['Code'] == "NoSuchKey":
                print("File Not Found yet")
            else:
                raise e





if __name__ == "__main__":
    app.run(debug=True)