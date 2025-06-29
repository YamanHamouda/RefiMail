#THIS FILE ISN'T ACTUALLY BEING RUN ANYWHERE IN THE REPO, BUT RATHER IT'S BEING RUN ON THE LAMDA INSTANCE

import json
import boto3
from bedrock_helper import call_bedrock

def lambda_handler(event, context):
    
    prompt = "Make this email {}, don't use all caps. Only return the email. You don't use --. You don't use \"I hope this email finds you well\" \n\n{}"
    



    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        file = response['Body']
        prompt_type = file.readline().decode('utf-8')
        email = file.read().decode('utf-8')
        
        response = call_bedrock((prompt_type,email))
        output_new_email(response)
        
        print("lamda finished")
        return response



    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def output_new_email(email):
    bucket = "yaman-hamouda-aws-lambda-hackathon-output"
    s3 = boto3.client('s3')
    file = _string_to_file(email)
    s3.upload_file("/tmp/output_email.txt", bucket, "output_email.txt")

def _string_to_file(email):
    file = open("/tmp/output_email.txt", "w")
    file.write(email)
    file.close()
    return file