#THIS FILE ISN'T ACTUALLY BEING RUN ANYWHERE IN THE REPO, BUT RATHER IT'S BEING RUN ON THE LAMDA INSTANCE

import boto3

def call_bedrock(prompt_and_email):
    prompt = "Make this email sound {}, don't use all caps. Only return the email. You don't use --. You don't use \"I hope this email finds you well\" \n\n{}"
    prompt = prompt.format(*prompt_and_email)


    modelId = "anthropic.claude-3-5-haiku-20241022-v1:0"
    message = generate_message(prompt)
    inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9}


    bedrock = boto3.client(service_name='bedrock-runtime',region_name = "us-west-2")
    print("calling bedrock")
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
