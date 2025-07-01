import boto3
def _string_to_file(email):
    file = open("src/email.txt", "w")
    file.write(email)
    file.close()
    return file

def _test_file():
    file = open("src/email.txt", "r")
    print("this should have the full email")
    print(file.read())
    file.close()

#yaman-hamouda-aws-lambda-hackathon-input
def send_email(email,id):
    bucket = "yaman-hamouda-aws-lambda-hackathon-input"
    s3 = boto3.client('s3')
    file = _string_to_file(email)
    #_test_file()
    s3.upload_file("src/email.txt",bucket,f"input_email{id}.txt")
    print("Email uploaded successfully")