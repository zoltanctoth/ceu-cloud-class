# %%
# Import required libraries
import boto3
from pathlib import Path
import pandas as pd
import os

# Set up AWS credentials
project_root = Path(__file__).parent.parent
keyfile = project_root / 'serverless' / 'accessKeys.csv'

if not keyfile.is_file():
    raise Exception("ERROR: AWS key file not found")

keyTable = pd.read_csv(keyfile)
AWS_ACCESS_KEY_ID = keyTable['Access key ID'][0]
AWS_SECRET_ACCESS_KEY = keyTable['Secret access key'][0]

os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
os.environ['AWS_DEFAULT_REGION'] = 'eu-west-1'

# Initialize the Amazon Translate client
translate_client = boto3.client('translate')

# %%
# Translate text from French to English
response = translate_client.translate_text(
    Text="Bonjour le monde!",
    SourceLanguageCode="fr",
    TargetLanguageCode="en"
)
print(response['TranslatedText'])

# %%
# Translate text from Spanish to English (auto-detect source language)
response = translate_client.translate_text(
    Text="Hola mundo!",
    SourceLanguageCode="auto",
    TargetLanguageCode="en"
)
print(response['TranslatedText'])

# %%
# Translate text to German (auto-detect source language)
long_text = ("Chronicles the experiences of a formerly successful banker as a prisoner "
             "in the gloomy jailhouse of Shawshank after being found guilty of a crime "
             "he did not commit. The film portrays the man's unique way of dealing "
             "with his new, torturous life; along the way he befriends a number of "
             "fellow prisoners, most notably a wise long-term inmate named Red.")
response = translate_client.translate_text(
    Text=long_text,
    SourceLanguageCode="auto",
    TargetLanguageCode="de"
)
print(response['TranslatedText'])

# %%
# Translate text from English to Hungarian
response = translate_client.translate_text(
    Text="The China–United States trade war is an ongoing economic conflict "
         "between the world’s two largest national economies, China and the United States",
    SourceLanguageCode="en",
    TargetLanguageCode="hu"
)
print(response['TranslatedText'])

