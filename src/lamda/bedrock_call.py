#THIS FILE ISN'T ACTUALLY BEING RUN ANYWHERE INT HE REPO, BUT RATHER IT'S BEING RUN ON THE LAMDA INSTANCE
import json
import boto3

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
        
        return response

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e



def output_new_email(email):
    bucket = "yaman-hamouda-aws-lambda-hackathon-output"
    s3 = boto3.client('s3')
    file = _string_to_file(email)
    s3.upload_file("output_email.txt", bucket, "output_email.txt")

def _string_to_file(email):
    file = open("output_email.txt", "w")
    file.write(email)
    file.close()
    return file



def call_bedrock(prompt_and_email):
    prompt = "Make this email {}, don't use all caps. Only return the email. You don't use --. You don't use \"I hope this email finds you well\" \n\n{}"
    prompt = prompt.format(*prompt_and_email)


    modelId = "anthropic.claude-3-5-haiku-20241022-v1:0"
    message = generate_message(prompt)
    inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9}


    bedrock = boto3.client(service_name='bedrock-runtime',region_name = "us-west-2")

    response = bedrock.converse(
        modelId=modelId,
        messages=message,
        inferenceConfig=inferenceConfig
    )
    response_text = response["output"]["message"]["content"][0]["text"] 
    return response_text

def generate_message(prompt_text):
    message = [
        {
            "role" : "user",
            "content" : [{"text": prompt_text  }]
        }
    ]
    return message
