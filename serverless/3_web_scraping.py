# %%
# Import required libraries for web scraping
print("📚 Setting up the environment...")

import requests
from bs4 import BeautifulSoup

print("✅ Libraries imported successfully")

# %%
# First, let's try without headers to demonstrate why they're needed
print("🌐 Attempting to access webpage without headers...")

url = "https://ceu.edu/article/2024-12-03/combining-data-science-society-thanika-haltrich-presidential-scholar-award"

try:
    response = requests.get(url)
    print(f"📡 Response status code: {response.status_code}")

    if response.status_code == 403:
        print("❌ Access forbidden! This demonstrates why we need proper headers.")
        print("ℹ️  Websites often block requests without proper User-Agent headers")
        print("   to prevent automated scraping.")
except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Now let's try with proper headers
print("🌐 Attempting to access webpage with proper headers...")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    print(f"📡 Response status code: {response.status_code}")

    if response.status_code != 200:
        raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

    content_length = len(response.content)
    print(f"✅ Successfully retrieved the webpage! Received {content_length} bytes of data.")
except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Parse the HTML and extract content
print("🔍 Parsing webpage content...")

try:
    # Parse the HTML
    webpage = BeautifulSoup(response.content, "html.parser")

    # Extract title
    title = webpage.title.string.strip()
    print("\n📑 Page Title:")
    print("-" * 40)
    print(title)
    print("-" * 40)

    # Extract paragraphs
    print("\n📝 Article Content:")
    print("-" * 40)
    description_html = webpage.select("#block-system-main p")  # <----------------- !!! Our selector !!!
    texts = [text.get_text().strip() for text in description_html]
    text = "\n".join(texts)
    print(text)
    print("-" * 40)

    print("\n✅ Content extracted successfully")
except Exception as e:
    print(f"❌ Error parsing content: {str(e)}")
