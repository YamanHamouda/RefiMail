import boto3
from botocore.exceptions import ClientError

from flask_cors import CORS
from flask import jsonify, Blueprint
import time


bp = Blueprint("S3_output",__name__)
CORS(bp)

@bp.route("/api/output", methods=["POST"])
def get_refined_email():
   email = get_email()
   print(email)
   
   return jsonify({ "new_email": email })
    


def get_email():
    for i in range(30):
        time.sleep(0.1)
        try:
            s3 = boto3.client("s3")
            bucket = "yaman-hamouda-aws-lambda-hackathon-output"
            key = "output_email.txt"

            s3_object = s3.get_object(Bucket=bucket, Key=key)
            file = s3_object['Body']
            new_email = file.read().decode('utf-8')
            return new_email
        except ClientError as e:
            if e.response['Error']['Code'] == "NoSuchKey":
                print("File Not Found yet")
            else:
                raise e


if __name__ == "__main__":
    bp.run(debug=True)