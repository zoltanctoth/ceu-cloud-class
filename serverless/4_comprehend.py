# %%
# Import
import pprint

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

pp = pprint.PrettyPrinter(indent=2)

apikey = ""
endpoint = "https://sentimenanalisisforpythonlearn.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(apikey))

# %%
# Language Detection
documents = ["This is a test sentence in English"]
response = text_analytics_client.detect_language(documents=documents)
pp.pprint(f"Language: {response[0].primary_language.name}")

documents = ["A: Hallo, wie geht es Ihnen?\nB: Ça va bien. Merci. Et toi?"]
response = text_analytics_client.detect_language(documents=documents)
pp.pprint(f"Language: {response[0]}")

# %%
# Sentiment Analysis
documents = [{"id": "1", "language": "en", "text": "Hey, I'm feeling great today!"}]
response = text_analytics_client.analyze_sentiment(documents)
pp.pprint(response[0])

# %%
# Sentiment Analysis
text = (
    "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse "
    "of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way "
    "of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably "
    "a wise long-term inmate named Red."
)

documents = [{"id": "1", "language": "en", "text": text}]
response = text_analytics_client.analyze_sentiment(documents)
pp.pprint(response[0])
print()

# %%
# ## Named Entity Recognition
documents = ["Amazon provides web services.", "Jeff is their leader."]
response = text_analytics_client.recognize_entities(documents)
for item in response:
    pp.pprint(item)
print()

# %%
# ## Key Phrase Detection
response = text_analytics_client.extract_key_phrases(documents)
for item in response:
    pp.pprint(item)

# %%
