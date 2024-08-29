# %%
# Imports

import os

import requests
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from bs4 import BeautifulSoup

# %%
# Scraping

response = requests.get(
    "https://ludic.mataroa.blog/blog/i-will-fucking-piledrive-you-if-you-mention-ai-again/")
response.raise_for_status()

webpage = BeautifulSoup(response.content, "html.parser")
article_html = webpage.select("h1, p:not(footer p)")

article_texts = [element.getText(strip=True) for element in article_html]
article_text = "\n".join(article_texts)
print(article_text)

# %%
# Get summaries

apikey = ""
endpoint = "https://sentimenanalisisforpythonlearn.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(apikey))

poller = text_analytics_client.begin_extract_summary(documents=[article_text])
summary_result = list(poller.result())

summaries = []

if summary_result and not summary_result[0].is_error:
    summaries = [sentence.text for sentence in summary_result[0].sentences]
elif summary_result:
    raise Exception(f"Error in document: {summary_result[0].error}")


# %%
# Create markdown file

with open('summaries.md', 'w', encoding='utf-8') as f:
    f.write('# Summaries\n\n')
    for summary in summaries:
        f.write(f'- {summary}\n')


# %%
# Remove markdown file

os.remove("summaries.md")
# %%
