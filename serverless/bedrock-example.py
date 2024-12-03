# %%
# This script demonstrates how to use Amazon Bedrock with role assumption
# We'll use the Titan model for text generation and track the associated costs

import json
import os
import pprint
from typing import Dict

import boto3

USE_LITE = False
# Pricing information for Titan models (as of March 2024)
# Source: https://aws.amazon.com/bedrock/pricing/
if USE_LITE:
    MODEL_ID = "amazon.titan-text-lite-v1"  # We use Titan Lite for cost-effective text generation
    COST_PER_INPUT_TOKEN = 0.0003 / 1000  # $0.0003 per 1,000 input tokens
    COST_PER_OUTPUT_TOKEN = 0.0004 / 1000  # $0.0004 per 1,000 output tokens
    print(f"🚀 Using Bedrock model {MODEL_ID}! This is a fast and cheap, but not super accurate model.")
else:
    MODEL_ID = "amazon.titan-text-express-v1"  # We use Titan Express for more advanced text generation
    COST_PER_INPUT_TOKEN = 0.001 / 1000  # $0.001 per 1,000 input tokens
    COST_PER_OUTPUT_TOKEN = 0.0017 / 1000  # $0.0017 per 1,000 output tokens
    print(f"🚀 Using Bedrock model {MODEL_ID}! This is a not so cheap, but quite accurate model.")

print()

print("📚 Setting up the environment...")
pp = pprint.PrettyPrinter(indent=2)
# AWS Configuration
# We need these constants to set up our AWS environment
ROLE_ARN = "arn:aws:iam::870137400553:role/BedrockUserRole"  # The role we'll assume to access Bedrock
REGION = "us-east-1"  # Bedrock is currently only available in specific regions

print("✅ Environment setup complete!")


def assume_role(role_arn: str, session_name: str) -> Dict[str, str]:
    """
    Assume an AWS IAM role to gain temporary security credentials.

    This function helps us access AWS services (like Bedrock) using temporary credentials
    obtained by assuming a role. It supports both AWS_PROFILE and default credentials.

    Args:
        role_arn (str): The Amazon Resource Name (ARN) of the role to assume
        session_name (str): A name for the assumed role session

    Returns:
        Dict[str, str]: Temporary credentials including AccessKeyId, SecretAccessKey, and SessionToken

    Raises:
        Exception: If role assumption fails due to permissions or network issues
    """
    print(f"🔐 Attempting to assume role: {role_arn}")

    try:
        # First, set up the initial AWS session
        # We check if a specific AWS profile is requested through environment variables
        if os.environ.get("AWS_PROFILE"):
            print(f"Using AWS Profile: {os.environ['AWS_PROFILE']}")
            session = boto3.Session(profile_name=os.environ["AWS_PROFILE"])
        else:
            print("Using default AWS credentials")
            session = boto3.Session()

        # Use STS (Security Token Service) to assume the role
        sts_client = session.client("sts")
        assumed_role = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
        print("✅ Role assumed successfully")
        return assumed_role["Credentials"]

    except Exception as e:
        print(f"❌ Error assuming role: {str(e)}")
        raise


print("✅ Function assume_role defined!")


def calculate_token_count(text: str) -> int:
    """
    Estimate the number of tokens in a text string.

    This is a rough estimation - actual token count may vary.
    We use a simple approximation of 4 characters per token.

    Args:
        text (str): The text to estimate tokens for

    Returns:
        int: Estimated number of tokens
    """
    return len(text) // 4


def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Calculate the cost of a Bedrock request based on input and output tokens.

    Args:
        input_tokens (int): Number of input tokens
        output_tokens (int): Number of output tokens

    Returns:
        float: Estimated cost in USD
    """
    input_cost = input_tokens * COST_PER_INPUT_TOKEN
    output_cost = output_tokens * COST_PER_OUTPUT_TOKEN
    return input_cost + output_cost


def send_message_to_bedrock(message: str, max_tokens: int = 512, temperature: float = 0.7) -> str:
    """
    Send a text generation request to Amazon Bedrock using the Titan model.

    This function handles the entire process of:
    1. Assuming the necessary AWS role
    2. Setting up a Bedrock client
    3. Sending the request
    4. Processing the response
    5. Calculating and displaying costs

    Args:
        message (str): The input text to send to the model
        max_tokens (int, optional): Maximum number of tokens in the response. Defaults to 512.
        temperature (float, optional): Controls randomness in the response.
            0.0 is deterministic, 1.0 is most random. Defaults to 0.7.

    Returns:
        str: The generated text response from the model

    Raises:
        Exception: If any step in the process fails
    """
    print("🚀 Preparing to send message to Bedrock...")
    print(f"\n📝 Input message: '{message}'")

    try:
        # Step 1: Get temporary credentials through role assumption
        credentials = assume_role(ROLE_ARN, "BedrockSession")

        # Step 2: Create a new AWS session with our temporary credentials
        session = boto3.Session(
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )

        # Step 3: Create Bedrock runtime client
        bedrock_runtime = session.client(service_name="bedrock-runtime", region_name=REGION)
        # Step 4: Prepare the request payload for the AI model
        payload = {
            # The actual text prompt we want to send to the model
            "inputText": message,
            # Configuration settings that control how the model generates text
            "textGenerationConfig": {
                # Maximum number of tokens (word pieces) in the response
                # Higher values allow longer responses but cost more
                # 512 tokens is roughly 350-400 words
                "maxTokenCount": max_tokens,
                # List of sequences that will stop the generation when encountered
                # Empty list means the model will continue until maxTokenCount
                # Example: [".", "?", "!"] would stop at the first sentence end
                "stopSequences": [],
                # Controls randomness in the response (between 0.0 and 1.0)
                # - Low values (0.0-0.3): More focused, deterministic responses
                # - Medium values (0.4-0.7): Balanced creativity
                # - High values (0.8-1.0): More random, creative responses
                "temperature": temperature,
                # Controls diversity of word choices (between 0.0 and 1.0)
                # 1.0 means consider all options
                # Lower values limit choices to only the most likely ones
                # Most users should leave this at 1.0
                "topP": 1,
            },
        }

        print("\n📦 Request configuration:")
        print(f"- Model: {MODEL_ID}")
        print(f"- Max tokens: {max_tokens}")
        print(f"- Temperature: {temperature}")

        # Calculate and display estimated input tokens and cost
        input_tokens = calculate_token_count(message)
        print("\n💰 Cost estimate (input):")
        print(f"- Input tokens: ~{input_tokens}")
        print(f"- Input cost: ${input_tokens * COST_PER_INPUT_TOKEN:.6f}")

        # Step 5: Send request to Bedrock
        response = bedrock_runtime.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload),
        )

        # Step 6: Process the response
        response_body = json.loads(response["body"].read())
        output_text = response_body["results"][0]["outputText"]

        # Calculate and display estimated output tokens and total cost
        output_tokens = calculate_token_count(output_text)
        total_cost = calculate_cost(input_tokens, output_tokens)

        print("\n💰 Final cost calculation:")
        print(f"- Output tokens: ~{output_tokens}")
        print(f"- Output cost: ${output_tokens * COST_PER_OUTPUT_TOKEN:.6f}")
        print(f"- Total cost: ${total_cost:.6f}")

        return output_text

    except Exception as e:
        print(f"❌ Error sending message to Bedrock: {str(e)}")
        raise


print("✅ Function send_message_to_bedrock defined!")


# %%
# Test the implementation with different prompts
# We'll try various types of requests to see how the model responds and track costs
test_message = "Write a haiku about data engineering"

try:
    print("-" * 40)
    response = send_message_to_bedrock(test_message)
    print("\n🤖 Titan's response:")
    print("-" * 40)
    print(response.strip())
    print("-" * 40)
except Exception as e:
    print(f"❌ Test failed: {str(e)}")

# %%
