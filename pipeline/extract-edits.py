import datetime
import json
import os

import boto3
import requests

# SUBJECT DATE
DATE_PARAM = "2022-10-28"
date = datetime.datetime.strptime(DATE_PARAM, "%Y-%m-%d")

# Wikimedia API URL formation
# See https://wikimedia.org/api/rest_v1/#/Edited%20pages%20data/get_metrics_edited_pages_top_by_edits__project___editor_type___page_type___year___month___day_
url = f"https://wikimedia.org/api/rest_v1/metrics/edited-pages/top-by-edits/en.wikipedia/user/content/{date.strftime('%Y/%m/%d')}"
print(f"Requesting REST API URL: {url}")

# Getting response from Wikimedia API
wiki_server_response = requests.get(url)
wiki_response_status = wiki_server_response.status_code
wiki_response_body = wiki_server_response.text

print(f"Wikipedia REST API Response body: {wiki_response_body}")
print(f"Wikipedia REST API Response Code: {wiki_response_status}")

# Check if response status is not OK
if wiki_response_status != 200:
    print(
        f"Received non-OK status code from Wiki Server: {wiki_response_status}. Response body: {wiki_response_body}"
    )

# Save Raw Response and upload to S3
RAW_LOCATION_BASE = "data/raw-edits"
os.makedirs(RAW_LOCATION_BASE, exist_ok=True)

# Saving the contents of `wiki_response_body` to a file
# The file is named in the format `raw-edits-YYYY-MM-DD.txt` and saved in the folder defined in `RAW_LOCATION_BASE`
raw_edits_filename = f"raw-edits-{date.strftime('%Y-%m-%d')}.txt"
raw_edits_fullpath = os.path.join(RAW_LOCATION_BASE, raw_edits_filename)
with open(raw_edits_fullpath, "w") as file:
    file.write(wiki_response_body)

########
# LAB  #
########
#
# Save the contents of `wiki_response_body` to file called `raw-edits-YYYY-MM-DD.txt` into the folder
# in variable `RAW_LOCATION_BASE` defined
# i.e: `data/raw-edits/raw-edits-2021-10-01.txt`.


########
# LAB  #
########
# Upload the file you created to S3.
# - Upload the file to your bucket (you can reuse your bucket from previous classes or create a new one).
# - Place the file in S3 under a folder called `datalake/raw/`.
# - Keep the file's name as `raw-edits-YYYY-MM-DD.txt`
# - Verify that the file is there (list the bucket in Python or on the AWS Website)

# BUCKET="{your bucket name}"
#
# {{ FILL IN AWS SETUP STEPS (you might need to copy your accessKey.csv to the working directory) }}
#

# Upload the file
# s3.upload_file("{{ ADD LOCAL FILE PATH }}", BUCKET, f'{{ ADD FOLDER AND FILE NAME HERE in a form of FOLDER/FILE_NAME }}"')

# END OF LAB

# Parse the Wikipedia response and process the data
wiki_response_parsed = wiki_server_response.json()
top_edits = wiki_response_parsed["items"][0]["results"][0]["top"]

# Convert server's response to JSON lines
current_time = datetime.datetime.now()
json_lines = ""
for page in top_edits:
    record = {
        "title": page["page_title"][0],
        "edits": page["edits"],
        "date": date.strftime("%Y-%m-%d"),
        "retrieved_at": current_time.isoformat(),
    }
    json_lines += json.dumps(record) + "\n"

# Save the Top Edits JSON lines and upload them to S3
JSON_LOCATION_BASE = "data/edits"
os.makedirs(JSON_LOCATION_BASE, exist_ok=True)

json_lines_filename = f"edits-{date.strftime('%Y-%m-%d')}.json"
json_lines_fullpath = os.path.join(JSON_LOCATION_BASE, json_lines_filename)

with open(json_lines_fullpath, "w") as file:
    file.write(json_lines)

# Upload the JSON file
s3.upload_file(json_lines_fullpath, BUCKET, f"datalake/edits/{json_lines_filename}")
