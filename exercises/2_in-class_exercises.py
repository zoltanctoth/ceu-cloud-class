# %%
# Initialize
import azure.cognitiveservices.speech as speechsdk
import requests
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from bs4 import BeautifulSoup

apikey_analytics = ""
endpoint = "https://sentimenanalisisforpythonlearn.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(
    endpoint, AzureKeyCredential(apikey_analytics))


def analyze_article(url, selector):
    response = requests.get(url)
    webpage = BeautifulSoup(response.content, "html.parser")
    article_html = webpage.select(selector)
    article_texts = [element.getText(strip=True) for element in article_html]
    article_text = "\n".join(article_texts)
    return text_analytics_client.analyze_sentiment(documents=[article_text])[0]


apikey_speech = ""
speech_config = speechsdk.SpeechConfig(
    subscription=apikey_speech,
    region='eastus',)
speech_config.speech_recognition_language = "en-US"

# %%
# Find an article on an English-language news site, scrape it, and check the sentiment using Python


url = "https://www.bbc.com/news/videos/c897lr34zpxo"
selector = "#main-content .fYAfXe , .kpWdWu"
sentiment = analyze_article(url, selector)
print(sentiment.confidence_scores)

# %%
# Find a comparable article on another English-language news site, scrape it, and compare the sentiment—idea: CNN vs. Fox News

url = "https://www.foxnews.com/us/small-tornado-reported-near-gary-indiana-midwestern-storm-onslaught"
selector = 'p:nth-child(14) , .ad-w-300+ p , .speakable+ p strong , .speakable'
sentiment = analyze_article(url, selector)
print(sentiment.confidence_scores)

# %%
# Find a comparable article on a non-English site, scrape it, and translate it to English with AWS translate. Then, compare sentiments.

url = "https://telex.hu/belfold/2024/06/09/szombathely-tornado-tolcser"
selector = '.article-html-content p , h1'
sentiment = analyze_article(url, selector)
print(sentiment.confidence_scores)

# %%
# Compare two news video
# My method get the first 15 sec only of the audio. We have to use start_continuous_recognition for detect the whole audio.
# Find two comparable news channels on YouTube.
# Download a news video from both in mp3, using (for example) https://ytmp3.nu/FlCn/.
# Use AWS transcribe to convert it to text and analyze the sentiment.
# https://www.youtube.com/watch?v=vNDXmG_FCMk&ab_channel=SkyNews
# https://www.youtube.com/watch?v=VV1nlMBEM0Y&ab_channel=9NewsAustralia


audio_config = speechsdk.audio.AudioConfig(filename="sky.wav")
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_config)

speech_recognition_result1 = speech_recognizer.recognize_once_async().get()
print(speech_recognition_result1.text)

audio_config = speechsdk.audio.AudioConfig(filename="aus.wav",)
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_config)
speech_recognition_result2 = speech_recognizer.recognize_once_async().get()
print(speech_recognition_result2.text)

# %%
# Sentiment analysis

sentiments = text_analytics_client.analyze_sentiment(
    documents=[speech_recognition_result1.text, speech_recognition_result2.text])
for sentiment in sentiments:
    print(sentiment.confidence_scores)
