#!/usr/bin/env python3
"""
Script to update lecture3_Serverless.md from R to Python examples
"""

import re

# Read the file
with open("lecture_notes/lecture3_Serverless.md", "r") as f:
    content = f.read()

# Update 1: Web Scraping - Replace everything from "IMDB Robots.txt" to the end of the ggplot code
old_web_scraping = r'''IMDB Robots\.txt: https://www\.imdb\.com/robots\.txt.*?```r\nlibrary\('ggplot2'\).*?geom_point\(aes\(size=Rating, col=Genre\)\)\n```'''

new_web_scraping = '''### Basic Web Scraping Example

```python
import requests
from bs4 import BeautifulSoup

# Set up headers to identify our request
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) "
    + " Chrome/39.0.2171.95 Safari/537.36"
}

# URL to scrape
url = "https://ceu.edu/article/2024-12-03/combining-data-science-society-thanika-haltrich-presidential-scholar-award"

# Fetch the webpage
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the HTML
    webpage = BeautifulSoup(response.content, "html.parser")

    # Extract title
    title = webpage.title.string.strip()
    print("Page Title:")
    print(title)

    # Extract paragraphs using CSS selector
    description_html = webpage.select("#block-system-main p")
    texts = [text.get_text().strip() for text in description_html]
    text = "\\n".join(texts)
    print("\\nArticle Content:")
    print(text)
else:
    print(f"Failed to fetch webpage: Status code {response.status_code}")
```

**Key Points:**
- Always include proper headers to avoid being blocked by websites
- Use CSS selectors (similar to `webpage.select()`) to target specific elements
- Check the website's `robots.txt` file to ensure scraping is allowed
- Be respectful of the website's resources and implement rate limiting if needed'''

content = re.sub(old_web_scraping, new_web_scraping, content, flags=re.DOTALL)

# Update 2: Amazon Polly section
old_polly = r'''### Installation\nTo install the Amazon Polly package in R:\n```r\ninstall\.packages\("aws\.polly".*?```r\nlibrary\("aws\.polly"\).*?play\(vec\)  # Play the synthesized speech\n```'''

new_polly = '''### Installation
To install the Amazon Polly SDK for Python (boto3):
```bash
pip install boto3
```

### Setting Up Credentials
You can set AWS credentials using environment variables or AWS CLI configuration:
```bash
aws configure
```

Or set them directly in Python:
```python
import os
os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_key"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
```

### Using Polly
To synthesize speech using Polly:
```python
import boto3
from io import BytesIO

# Create Polly client
polly = boto3.client('polly', region_name='us-east-1')

# Synthesize speech
text = "Forget that! There are places in this world that aren't made out of stone..."
response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joey'
)

# Save the audio stream
if "AudioStream" in response:
    with open("output.mp3", "wb") as file:
        file.write(response["AudioStream"].read())
    print("Speech synthesized successfully!")
```'''

content = re.sub(old_polly, new_polly, content, flags=re.DOTALL)

# Write the updated content
with open("lecture_notes/lecture3_Serverless.md", "w") as f:
    f.write(content)

print("✅ Updated lecture3_Serverless.md with Python examples")
