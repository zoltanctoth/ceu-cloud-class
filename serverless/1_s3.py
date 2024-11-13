# %%
import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()
print(response)

# %%
import pprint

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(response)

# %%
for r in response["Buckets"]:
    print(r["Name"])

# %%
# Creating a unique S3 bucket name
import random
import string

# !! CHANGE THIS:
my_name = "add-your-name-here-3"  # !! Replace with your name
# !!

random_part = "".join(random.choices(string.digits, k=3))
bucket_name = f"{my_name}-{random_part}"
print(f"Bucket name: {bucket_name}")

# %%
default_region = s3.meta.region_name
print(f"Default region: {default_region}")

# %%
bucket_configuration = {"LocationConstraint": default_region}
response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=bucket_configuration)

assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
print(f"Bucket {bucket_name} created in {default_region}")
pp.pprint(response)

# %%
# Bucket location
response = s3.get_bucket_location(Bucket=bucket_name)
print(f"Bucket location: {response['LocationConstraint']}")

# %%
# Creating a sample text file
with open("my_content.txt", "w") as file:
    file.write("This is a simple text file")

# %%
# Send the text file to your AWS S3 bucket
response = s3.upload_file("my_content.txt", bucket_name, "my_content.txt")
print(f"File uploaded to S3. Location: s3://{bucket_name}/my_content.txt")

# %%
# Save files from S3 to your computer
s3.download_file(bucket_name, "my_content.txt", "my_content_downloaded.txt")

# %%
# Display file contents
with open("my_content_downloaded.txt", "r") as file:
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
# Finally, delete the file you created
import os

os.remove("my_content.txt")
os.remove("my_content_downloaded.txt")
