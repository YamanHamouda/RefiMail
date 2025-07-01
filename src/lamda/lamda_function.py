import json
import boto3
from bedrock_helper import call_bedrock
s3 = boto3.client('s3')
bucket = "yaman-hamouda-aws-lambda-hackathon-output"

def lambda_handler(event, context):


    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        filename = key
        file = response['Body']
        #11 because input_email is 11 characters long
        id = filename[11:len(filename)-4] # len(filename) - 4 for the .txt
        prompt_type = file.readline().decode('utf-8')
        email = file.read().decode('utf-8')
        
        response = call_bedrock((prompt_type,email))
        output_new_email(response,id)
        
        print("lamda finished")
        return response



    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def output_new_email(email,id):
    s3.put_object(Body=email, Bucket=bucket, Key=f"output_email{id}.txt")
    # file = _string_to_file(email)
    # print(id)
    # s3.upload_file("/tmp/output_email.txt", bucket, f"output_email{id}.txt")

def _string_to_file(email):
    file = open("/tmp/output_email.txt", "w")
    file.write(email)
    file.close()
    return file



