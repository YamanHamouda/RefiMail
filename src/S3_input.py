import boto3
import boto3
session = boto3.session.Session()
credentials = session.get_credentials()
print(credentials)
def _string_to_file(email):
    file = open("email.txt", "w")
    file.write(email)
    return file

#yaman-hamouda-aws-lambda-hackathon-input
def send_email(email):
    bucket = "yaman-hamouda-aws-lambda-hackathon-input"
    s3 = boto3.client('s3')
    file = _string_to_file(email)
    s3.upload_file("email.txt",bucket,"email.txt")