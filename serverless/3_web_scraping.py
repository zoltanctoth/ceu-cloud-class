# %%

import requests
from bs4 import BeautifulSoup

# %%
# Specifying the URL

# Point and click selector: https://selectorgadget.com/
url = "https://edition.cnn.com/style/article/egypt-temple-cleopatra-lost-tomb-scli-intl-scn/index.html"

# Sending a request to the webpage
response = requests.get(url)

# Ensure the request was successful
if response.status_code != 200:
    raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

# %%

# Parsing the HTML content
webpage = BeautifulSoup(response.content, "html.parser")
# Using CSS selectors to scrape the section
description_html = webpage.select(".article__content")
texts = [text.get_text().strip() for text in description_html]
text = "\n".join(texts)

print(text)
