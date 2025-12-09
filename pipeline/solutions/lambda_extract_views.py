import datetime
import json

import boto3
import requests

# Set your username here - must match the bucket created in the notebook
# Bucket name: <username>-wikidata
# Database name: <username> (used in Athena SQL files)
S3_WIKI_BUCKET = "zoltanctothceu-wikidata"


def lambda_handler(event, context):
    """
    Lambda handler for Wikipedia page views ETL pipeline.

    Optional date parameter: {"date": "2025-11-25"}
    If not provided, defaults to 21 days ago.
    """
    # Get date from event, or default to 21 days ago
    date_str = event.get("date")
    if date_str:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    else:
        date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=21)

    # Extract: fetch from Wikipedia Page Views API
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/{date.strftime('%Y/%m/%d')}"
    response = requests.get(url, headers={"User-Agent": "curl/7.68.0"})

    if response.status_code != 200:
        raise Exception(f"Wikipedia API error: {response.status_code} - {response.text}")

    # Transform: convert to JSON Lines
    top_views = response.json()["items"][0]["articles"]
    current_time = datetime.datetime.now(datetime.timezone.utc)

    json_lines = ""
    for page in top_views:
        record = {
            "title": page["article"],
            "views": page["views"],
            "rank": page["rank"],
            "date": date.strftime("%Y-%m-%d"),
            "retrieved_at": current_time.replace(tzinfo=None).isoformat(),
        }
        json_lines += json.dumps(record) + "\n"

    # Load: upload to S3
    s3 = boto3.client("s3")
    s3_key = f"raw-views/raw-views-{date.strftime('%Y-%m-%d')}.json"
    s3.put_object(Bucket=S3_WIKI_BUCKET, Key=s3_key, Body=json_lines)

    return {
        "statusCode": 200,
        "body": f"Uploaded {len(top_views)} records to s3://{S3_WIKI_BUCKET}/{s3_key}",
    }
