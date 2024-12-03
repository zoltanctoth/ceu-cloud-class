# %%
# Import required libraries and set up our environment
# We'll use these throughout the tutorial to interact with AWS S3
import os
import pprint
import random
import string

import boto3

print("📚 Setting up the environment...")

# Initialize pretty printer for better output formatting
pp = pprint.PrettyPrinter(indent=2)

# Create S3 client using default credentials from AWS CLI
# boto3 will automatically use credentials from ~/.aws/credentials
s3 = boto3.client(
    "s3",
    region_name="eu-west-1",  # Ireland region
)

print("✅ Environment setup complete!")
print(f"🌍 Using AWS region: {s3.meta.region_name}")

# %%
# Let's first check what buckets already exist in your AWS account
# This helps us understand what resources we're starting with
print("📋 Listing all S3 buckets in your account...")
response = s3.list_buckets()

print("\n📦 Raw response from AWS:")
pp.pprint(response)

print("\n📦 Your current S3 buckets:")
if response["Buckets"]:
    for bucket in response["Buckets"]:
        print(f"- {bucket['Name']}")
else:
    print("No buckets found in your account")

print(f"\n✅ Successfully retrieved {len(response['Buckets'])} buckets")

# %%
# Now we'll create a function to generate unique bucket names
# S3 bucket names must be globally unique across all AWS accounts
print("🔧 Setting up bucket name generator...")


def generate_bucket_name(base_name):
    """Generate a unique bucket name using base name and random digits"""
    random_part = "".join(random.choices(string.digits, k=3))
    return f"{base_name}-{random_part}"


# Generate a unique bucket name - replace 'add-your-name-here' with your name!
my_name = "add-your-name-here"  # TODO: Change this!
bucket_name = generate_bucket_name(my_name)

if my_name == "add-your-name-here":
    print("❌ Remember to change 'add-your-name-here' to your actual name!")
else:
    print("✅ Name generator ready")
    print(f"📝 Your generated bucket name: {bucket_name}")

# %%
# Create a new S3 bucket with our generated name
# We'll specify EU (Ireland) as our region
default_region = "eu-west-1"
print(f"🚀 Creating new bucket: {bucket_name}")
print(f"🌍 Region: {default_region}")

try:
    # Note: Bucket configuration is required for all regions except us-east-1
    bucket_configuration = {"LocationConstraint": default_region}
    response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=bucket_configuration)

    print("\n📦 AWS Response:")
    pp.pprint(response)

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print(f"\n✅ Success! Bucket {bucket_name} created in {default_region}")
except Exception as e:
    print(f"❌ Error creating bucket: {str(e)}")

# %%
# Create a sample text file that we'll upload to S3
# This demonstrates creating and uploading content to our bucket
print("📝 Creating sample file...")

sample_content = """Hello from AWS S3!
This is a sample file created during the class.
You can modify this content to upload different text."""

try:
    with open("my_content.txt", "w") as file:
        file.write(sample_content)
    print("✅ Sample file created locally")
    print(f"📄 File contents ({len(sample_content)} characters):")
    print("-" * 40)
    print(sample_content)
    print("-" * 40)
except Exception as e:
    print(f"❌ Error creating file: {str(e)}")

# %%
# Upload our file to S3
# This shows how to transfer local files to your S3 bucket
print(f"⬆️  Uploading file to bucket: {bucket_name}")

try:
    s3.upload_file("my_content.txt", bucket_name, "my_content.txt")
    print("✅ Upload successful!")
    print(f"📍 File location: s3://{bucket_name}/my_content.txt")
    print(f"ℹ️ Note: The https URL https://{bucket_name}.s3.eu-west-1.amazonaws.com/my_content.txt")
    print("   won't work directly because S3 objects are private by default!")
    print("   We'll generate a pre-signed URL later to access this file via HTTPS.")

    # Verify the upload by listing objects in the bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)
    print("\n📦 Current bucket contents:")
    for obj in objects.get("Contents", []):
        print(f"- {obj['Key']} ({obj['Size']} bytes)")
except Exception as e:
    print(f"❌ Error uploading file: {str(e)}")

# %%
# Generate a pre-signed URL for temporary access to the file
# This allows others to download the file without AWS credentials
print("🔗 Generating pre-signed URL...")

try:
    # Generate URL that expires in 1 hour (3600 seconds)
    presigned_url = s3.generate_presigned_url(
        "get_object", Params={"Bucket": bucket_name, "Key": "my_content.txt"}, ExpiresIn=3600
    )
    print("✅ Pre-signed URL generated successfully!")
    print("\n📎 URL Details:")
    print(f"- URL: {presigned_url}")
    print("- Expires in: 1 hour")
    print("- Anyone with this URL can download the file")
    print("ℹ️  Note: You can adjust ExpiresIn for different durations")
except Exception as e:
    print(f"❌ Error generating pre-signed URL: {str(e)}")

# %%
# Download the file we just uploaded
# This verifies our upload worked and shows how to retrieve files from S3
print("⬇️  Downloading file from S3...")

try:
    s3.download_file(bucket_name, "my_content.txt", "my_content_downloaded.txt")
    print("✅ Download successful!")

    # Display the contents to verify everything worked
    with open("my_content_downloaded.txt", "r") as file:
        downloaded_content = file.read()

    print("\n📄 Downloaded file contents:")
    print("-" * 40)
    print(downloaded_content)
    print("-" * 40)

    # Verify content matches
    if downloaded_content == sample_content:
        print("✅ Content verification: Downloaded file matches original!")
    else:
        print("❌ Content verification: Files don't match!")
except Exception as e:
    print(f"❌ Error downloading file: {str(e)}")

# %%
# Clean up all resources we created
# This is important to avoid unnecessary AWS charges and maintain a clean workspace
print("🧹 Starting cleanup process...")


def cleanup_resources():
    """Clean up all resources created during this tutorial"""
    cleanup_report = []

    try:
        # 1. Delete the object from S3
        print(f"🗑️  Deleting object from bucket {bucket_name}...")
        s3.delete_object(Bucket=bucket_name, Key="my_content.txt")
        cleanup_report.append("✅ S3 object deleted")

        # 2. Delete the bucket
        print(f"🗑️  Deleting bucket {bucket_name}...")
        s3.delete_bucket(Bucket=bucket_name)
        cleanup_report.append("✅ S3 bucket deleted")

        # 3. Delete local files
        local_files = ["my_content.txt", "my_content_downloaded.txt"]
        for file in local_files:
            if os.path.exists(file):
                os.remove(file)
                cleanup_report.append(f"✅ Deleted local file: {file}")

        print("\n📋 Cleanup Report:")
        for item in cleanup_report:
            print(item)
        print("\n✨ All cleanup completed successfully!")

    except Exception as e:
        print(f"❌ Error during cleanup: {str(e)}")
        print("⚠️  Some resources might need manual cleanup!")


# Execute the cleanup
cleanup_resources()

# Verify all buckets after cleanup
print("\n🔍 Verifying cleanup - listing remaining buckets:")
final_buckets = s3.list_buckets()["Buckets"]
if not any(b["Name"] == bucket_name for b in final_buckets):
    print("✅ Bucket successfully removed!")
else:
    print("⚠️  Bucket still exists - might need manual removal!")
