import json
import os

import boto3


def assume_role(role_arn, session_name):
    if os.environ.get("AWS_PROFILE"):
        session = boto3.Session(profile_name=os.environ["AWS_PROFILE"])
    else:
        session = boto3.Session()
    sts_client = session.client("sts")
    assumed_role = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
    return assumed_role["Credentials"]


def send_message_to_bedrock(message):
    role_arn = "arn:aws:iam::870137400553:role/BedrockUserRole"
    credentials = assume_role(role_arn, "BedrockSession")

    session = boto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )

    bedrock_runtime = session.client(
        service_name="bedrock-runtime", region_name="us-east-1"  # Replace with your preferred region
    )

    payload = {
        "inputText": message,
        "textGenerationConfig": {"maxTokenCount": 512, "stopSequences": [], "temperature": 0.7, "topP": 1},
    }

    response = bedrock_runtime.invoke_model(
        modelId="amazon.titan-text-lite-v1",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload),
    )

    response_body = json.loads(response["body"].read())
    return response_body["results"][0]["outputText"]


if __name__ == "__main__":
    message = "hello"
    response = send_message_to_bedrock(message)
    print(f"Response from Bedrock: {response}")
