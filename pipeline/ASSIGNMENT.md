# Assignment: Wikipedia Page Views Pipeline

Build a data pipeline for Wikipedia page views, similar to what we did for edits.

## Overview

You will:
1. Create a notebook that extracts top viewed Wikipedia pages
2. Create Athena tables to query the data
3. Deploy as a Lambda function
4. Schedule with EventBridge

**Use the same `<username>` you used for the edits pipeline!**

## Part 1: Create the Notebook

Create a new notebook in `/homework/extract_views.ipynb` that extracts, transforms, and loads page view data.

**API Documentation:** https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/reference/page-views.html

Look for the endpoint that returns the **most-viewed pages** for a given day.

Your notebook should:
1. Fetch the top viewed pages for a specific date
2. Transform the response to JSON Lines format with these fields:
   - `title` - the article title
   - `views` - the view count
   - `rank` - the ranking position
   - `date` - the date being queried
   - `retrieved_at` - timestamp when you fetched the data
3. Upload to S3 at `raw-views/raw-views-YYYY-MM-DD.json`

Use the same bucket as edits: `<username>-wikidata`

**Tip:** The API response structure is slightly different from the edits API. Explore the response JSON to find where the article data is located.

## Part 2: Create Athena Tables

Create two SQL files:

1. `4_raw_views.sql` - External table called `raw_views` pointing to your S3 data
2. `5_views_view.sql` - View called `views` with proper timestamp casting + **records ordered by `date` (primary, ascending) and `rank` (secondary, ascending)**.

Look at `2_raw_edits.sql` and `3_edits_view.sql` for reference. Your table columns should match the JSON fields from Part 1.

## Part 3: Create Lambda Function

1. Create `lambda_extract_views.py` (convert the logic of your notebook)
   - The Lambda should default to fetching data from 21 days ago if no date is provided
   - Accept an optional `{"date": "YYYY-MM-DD"}` parameter to fetch a specific date

2. Deploy to AWS Lambda
   - **Function name:** `WikiViewsLambda<Username>` (e.g., `WikiViewsLambdaJohndoe`)
   - **Runtime:** Python 3.13
   - Add the `AWSSDKPandas-Python313` layer (from AWS layers, not custom ARN)
   - Attach the `LambdaS3ExecutionRole` role (or create a role with S3 write access)
   - Set timeout to 30 seconds

3. Test both with `{"date": "2025-11-20"}` and with `{}` (empty event) - this will use the default date (21 days ago)

## Part 4: Schedule with EventBridge

1. Go to Amazon EventBridge → Schedules → Create schedule
2. Configure:
   - **Schedule name:** `WikiViewsScheduler<Username>` (e.g., `WikiViewsSchedulerJohndoe`)
   - **Schedule type:** Recurring schedule
   - **Cron expression:** `0 6 * * ? *` (daily at 6 AM UTC)
   - **Flexible time window:** Off
   - **Target:** AWS Lambda → your Lambda function
   - **Payload:** `{}`
   - **Role:** Create new role or use `EventBridgeLambdaRole`

## Deliverables

In your `/homework` folder on GitHub:
1. `extract_views.ipynb` - the notebook
2. `lambda_extract_views.py` - the Lambda code
3. `4_raw_views.sql` - table creation SQL
4. `5_views_view.sql` - view creation SQL
5. Screenshots showing:
   - Lambda function tested successfully (should show `statusCode: 200`)
   - EventBridge schedule created
   - Athena query results executing `SELECT * FROM views` view

## Grading Criteria
Ensure that all assets you submit check all the requirements above:
1) Homework in the `homework` folder on Git, committed and pushed to GitHub
2) You use the same username, bucket, and database as in your in-class exercise
3) Notebook in place and checks every requirement above
4) SQL files in place and check all requirements above
5) Lambda function in place and checks all requirements above
6) Lambda function deployed under the function name required and works both with and without passing a date parameter
7) EventBridge created with the schedule name required
