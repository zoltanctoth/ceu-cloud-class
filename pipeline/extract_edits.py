# %% Verification Functions
import datetime
import json
from pathlib import Path

import boto3
import requests


def verify_lab1_solution(file_path, content):
    """Verifies the lab 1 solution for saving raw Wikipedia data"""
    try:
        # Check directory
        print(f"📁 Checking folder {RAW_LOCATION_BASE}...")
        if not RAW_LOCATION_BASE.exists():
            print("❌ Required folder does not exist")
            return False
        print(f"✅ Folder {RAW_LOCATION_BASE} exists!")

        # Check if file exists
        print(f"📄 Checking file {file_path}...")
        if not file_path.exists():
            print("❌ File does not exist")
            return False
        print(f"✅ File {file_path.name} exists!")

        # Check file name format
        print("🔍 Checking file name format...")
        expected_name = f"raw-edits-{date.strftime('%Y-%m-%d')}.txt"
        if file_path.name != expected_name:
            print(f"❌ Incorrect file name. Expected: {expected_name}")
            return False
        print(f"✅ File name matches expected format: {expected_name}")

        # Check file content
        print("📝 Checking file content...")
        with file_path.open("r") as f:
            file_content = f.read()
            if file_content != content:
                print("❌ File content does not match expected content")
                return False
        print("✅ File content matches expected data!")

        # Check file location
        print("📍 Checking file location...")
        if str(RAW_LOCATION_BASE) not in str(file_path):
            print("❌ File not saved in correct directory")
            return False
        print("✅ File is in the correct directory!")

        print("🌟 All checks passed for Lab 1!")
        return True

    except Exception as e:
        print(f"❌ Error during verification: {str(e)}")
        return False


def verify_bucket_name(bucket_name):
    """Verifies the S3 bucket name format"""
    try:
        print("🔍 Checking bucket name format...")

        # Check if bucket name is empty or default
        if not bucket_name or bucket_name == "<>":
            print("❌ Bucket name cannot be empty or default '<>'")
            return False
        print("✅ Bucket name is not empty!")

        # Check if bucket name ends with -wikidata
        if not bucket_name.endswith("-wikidata"):
            print("❌ Bucket name must end with '-wikidata'")
            return False
        print("✅ Bucket name ends with '-wikidata'!")

        # Check minimum length
        name_without_suffix = bucket_name[:-9]  # Remove '-wikidata'
        if len(name_without_suffix) < 3:
            print("❌ Bucket name too short (excluding '-wikidata')")
            return False
        print("✅ Bucket name has valid length!")

        print("🌟 Bucket name format is correct!")
        return True

    except Exception as e:
        print(f"❌ Error during bucket name verification: {str(e)}")
        return False


def verify_s3_upload(bucket, key, local_file):
    """Verifies the S3 upload was successful"""
    try:
        print("🔍 Checking S3 upload...")

        # Check if file exists in S3
        try:
            print(f"📡 Checking if file exists in S3 bucket {bucket}...")
            s3_obj = s3.head_object(Bucket=bucket, Key=key)
            print("✅ File found in S3!")
        except Exception:
            print("❌ File not found in S3")
            return False

        # Check prefix
        print("📁 Checking S3 folder structure...")
        if not key.startswith("datalake/raw/"):
            print("❌ Incorrect S3 prefix. Must be 'datalake/raw/'")
            return False
        print("✅ File is in correct S3 folder!")

        # Check file sizes match
        print("📊 Checking file sizes...")
        local_size = local_file.stat().st_size
        s3_size = s3_obj["ContentLength"]
        if local_size != s3_size:
            print("❌ File size mismatch between local and S3")
            return False
        print(f"✅ File sizes match: {local_size} bytes!")

        # Check path format
        print("🔍 Checking S3 path format...")
        expected_key = f"datalake/raw/raw-edits-{date.strftime('%Y-%m-%d')}.txt"
        if key != expected_key:
            print(f"❌ Incorrect S3 key format. Expected: {expected_key}")
            return False
        print("✅ S3 path format is correct!")

        print("🌟 All S3 upload checks passed!")
        return True

    except Exception as e:
        print(f"❌ Error during S3 verification: {str(e)}")
        return False


# %% Retrieve data from Wikipedia
# SUBJECT DATE ### TRY A FEW OF THIS IN CLASS
DATE_PARAM = "2024-11-25"

date = datetime.datetime.strptime(DATE_PARAM, "%Y-%m-%d")

# Wikimedia API URL formation
# =============================================================================
# Docs: https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/reference/edits.html#list-most-edited-pages-by-number-of-edits
# =============================================================================
url = f"https://wikimedia.org/api/rest_v1/metrics/edited-pages/top-by-edits/en.wikipedia/user/content/{date.strftime('%Y/%m/%d')}"
print(f"Requesting REST API URL: {url}")

# Getting response from Wikimedia API
wiki_server_response = requests.get(url, headers={"User-Agent": "curl/7.68.0"})
wiki_response_status = wiki_server_response.status_code
wiki_response_body = wiki_server_response.text

print(f"Wikipedia REST API Response body: {wiki_response_body}")
print(f"Wikipedia REST API Response Code: {wiki_response_status}")

# Check if response status is not OK
if wiki_response_status != 200:
    print(
        f"❌ Received non-OK status code from Wiki Server: {wiki_response_status}. Response body: {wiki_response_body}"
    )
else:
    print(f"✅ Successfully retrieved Wikipedia data, content-length: {len(wiki_response_body)}")

# %% Set up local directory structure
current_directory = Path(__file__).parent
RAW_LOCATION_BASE = current_directory / "data" / "raw-edits"
RAW_LOCATION_BASE.mkdir(exist_ok=True, parents=True)
print(f"Created directory {RAW_LOCATION_BASE}")

# %% LAB
#########
# LAB 1 #
#########
# Save the contents of `wiki_response_body` to file called `raw-edits-YYYY-MM-DD.txt` in the folder
# in variable `RAW_LOCATION_BASE`.
# i.e: `data/raw-edits/raw-edits-2024-10-01.txt`.
# Store the path to the file in the variable `raw_edits_file`.

# YOUR SOLUTION COMES HERE =========================
raw_edits_file = ""  # Placeholder, feel free to remove this

# ==================================================

# Verify solution
if verify_lab1_solution(raw_edits_file, wiki_response_body):
    print("🎉 Lab 1 completed successfully!")
else:
    print("❌ Lab 1 needs correction")

# %% LAB
#########
# LAB 2 #
#########
S3_WIKI_BUCKET = "<>"
# Create a new bucket for your wikipedia pipeline
# > Choose a name ending with "-wikidata"
# > Store the bucket name in the variable S3_WIKI_BUCKET
# > Create the bucket if it does not exist
s3 = boto3.client("s3")

# YOUR SOLUTION COMES HERE =========================

# ==================================================

if not verify_bucket_name(S3_WIKI_BUCKET):
    raise ValueError("Invalid bucket name")

# Verify bucket access
try:
    s3.head_bucket(Bucket=S3_WIKI_BUCKET)
    print("✅ Bucket is accessible")
except Exception as e:
    print(f"❌ Cannot access bucket: {str(e)}")
    raise

# %% LAB
#########
# LAB 3 #
#########
# Upload the file you created to S3.
# - Place the file in S3 under a folder called `datalake/raw/`.
# - Keep the file's name as `raw-edits-YYYY-MM-DD.txt` (where YYYY-MM-DD is the date of the file).
#   > Don't hardcode the date. Calculate it from the DATE_PARAM variable.
# - Verify that the file is there (list the bucket in Python or on the AWS Website)
# Store the S3 key in the variable `s3_key`. The S3 Key here is the s3 URL's part after the bucket name.

# YOUR SOLUTION COMES HERE =========================

s3_key = ""  # Placeholder, feel free to remove this

# ==================================================


print(f"Uploaded raw edits to s3://{S3_WIKI_BUCKET}/{s3_key}")

# Verify upload
if verify_s3_upload(S3_WIKI_BUCKET, s3_key, raw_edits_file):
    print("🎉 Lab 3 completed successfully!")
else:
    print("❌ Lab 3 needs correction")

# END OF LAB

# %% Process and transform the data
wiki_response_parsed = wiki_server_response.json()
top_edits = wiki_response_parsed["items"][0]["results"][0]["top"]

current_time = datetime.datetime.now(datetime.timezone.utc)  # Always use UTC!!
json_lines = ""
for page in top_edits:
    record = {
        "title": page["page_title"],
        "edits": page["edits"],
        "date": date.strftime("%Y-%m-%d"),
        "retrieved_at": current_time.replace(
            tzinfo=None
        ).isoformat(),  # We need to remove tzinfo as Athena cannot work with offsets
    }
    json_lines += json.dumps(record) + "\n"

JSON_LOCATION_DIR = current_directory / "data" / "edits"
JSON_LOCATION_DIR.mkdir(exist_ok=True, parents=True)
print(f"Created directory {JSON_LOCATION_DIR}")
print(f"JSON lines:\n{json_lines}")

# %% Save and upload processed data
json_lines_filename = f"edits-{date.strftime('%Y-%m-%d')}.json"
json_lines_file = JSON_LOCATION_DIR / json_lines_filename

with json_lines_file.open("w") as file:
    file.write(json_lines)

s3.upload_file(json_lines_file, S3_WIKI_BUCKET, f"datalake/bronze_edits/{json_lines_filename}")
print(f"✅ Uploaded processed data to s3://{S3_WIKI_BUCKET}/datalake/bronze_edits/{json_lines_filename}")

# %%
