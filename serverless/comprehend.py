# %% [markdown]
# ## Setting up AWS Credentials

# %%
import os
from pathlib import Path

import boto3
import pandas as pd

# Explicitly set the path to the 'serverless' directory
project_root = Path(__file__).parent.parent  # This goes up two levels from the current script's directory
# Load AWS keys from a file in the script directory
keyfile = project_root / 'serverless' / 'accessKeys.csv'


if not keyfile.is_file():
    raise Exception("ERROR: AWS key file not found")

keyTable = pd.read_csv(keyfile)
AWS_ACCESS_KEY_ID = keyTable['Access key ID'][0]
AWS_SECRET_ACCESS_KEY = keyTable['Secret access key'][0]

# Set environment variables for AWS access
os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY
os.environ['AWS_DEFAULT_REGION'] = 'eu-west-1'

# %%
# Language Detection
comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')

# Detect language
text = "This is a test sentence in English"
print(comprehend.detect_dominant_language(Text = text))

# %%
# Multi-lingual Language Detection
text = "A: ¡Hola! ¿Como está, usted?\nB: Ça va bien. Merci. Et toi?"
print(comprehend.detect_dominant_language(Text = text))


# %%
# Sentiment Analysis
text = "Hey, I'm feeling great today!"
print(comprehend.detect_sentiment(Text=text, LanguageCode='en'))

# %%
# Sentiment Analysis
text = ("Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse "
        "of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way "
        "of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably "
        "a wise long-term inmate named Red.")
print(comprehend.detect_sentiment(Text=text, LanguageCode='en'))


# %%
# ## Named Entity Recognition
texts = ["Amazon provides web services.", "Jeff is their leader."]
for text in texts:
    print(comprehend.detect_entities(Text=text, LanguageCode='en'))

# %%
# ## Key Phrase Detection
for text in texts:
    print(comprehend.detect_key_phrases(Text=text, LanguageCode='en'))

# %%
