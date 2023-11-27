# %%
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# %%
# Specifying the URL
url = 'https://edition.cnn.com/style/article/egypt-temple-cleopatra-lost-tomb-scli-intl-scn/index.html'

# Sending a request to the webpage
response = requests.get(url)

# Ensure the request was successful
if response.status_code != 200:
    raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

# Parsing the HTML content
webpage = BeautifulSoup(response.content, 'html.parser')

# %%
# Using CSS selectors to scrape the section
description_html = webpage.select('.article__content')

# Converting the data to text
description = [element.get_text() for element in description_html]

# Print the description
for desc in description:
    print(desc)

# %%
