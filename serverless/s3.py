# %%
# Installation (Python equivalent)
# In Python, boto3 is used to interact with AWS services like S3.
# You can install it using pip.
# Run this in your terminal or VS Code's terminal:
# pip install boto3

# %%
# Set up Python with AWS
import os
from pathlib import Path
import pandas as pd

# Locate the accessKeys.csv file
keyfile = list(Path(".").glob("accessKeys.csv"))
if not keyfile:
    raise Exception("ERROR: AWS key file not found")
keyfile = keyfile[0] 

# Read the AWS keys
keyTable = pd.read_csv(keyfile)
AWS_ACCESS_KEY_ID = keyTable['Access key ID'].iloc[0]
AWS_SECRET_ACCESS_KEY = keyTable['Secret access key'].iloc[0]

# Set environment variables for AWS access
os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
os.environ['AWS_DEFAULT_REGION'] = 'eu-west-1'

# %%
# Have a look at your buckets on AWS
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print(buckets)

# %%
# Creating a unique S3 bucket name
import random
import string

my_name = "mike"  # Replace with your name
random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
bucket_name = f"{my_name}-{random_part}"
print(bucket_name)

# %%
# Now, create the bucket on S3
bucket_configuration = {
    'LocationConstraint': os.environ['AWS_DEFAULT_REGION']
}
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=bucket_configuration)

# %%
# Bucket location
response = s3.get_bucket_location(Bucket=bucket_name)
print(response['LocationConstraint'])

# %%
# Creating a sample text file
with open("my_content.txt", "w") as file:
    file.write("This is a simple text file")

# %%
# Send the text file to your AWS S3 bucket
s3.upload_file("my_content.txt", bucket_name, "my_content.txt")

# %%
# Save files from S3 to your computer
s3.download_file(bucket_name, "my_content.txt", "my_content_s3.txt")

# %%
# Check the file
import os

print(os.listdir('.'))

# %%
# Display file contents
with open("my_content_s3.txt", "r") as file:
    content = file.read()
print(content)

# %%
# Deleting S3 objects:
s3.delete_object(Bucket=bucket_name, Key="my_content.txt")

# %%
# Deleting buckets
# Note: The bucket must be empty before it can be deleted.
s3.delete_bucket(Bucket=bucket_name)

# %%
# Try to delete it again. You will see an error!
try:
    s3.delete_bucket(Bucket=bucket_name)
except Exception as e:
    print(e)

# %%
