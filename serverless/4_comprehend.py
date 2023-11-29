# %% [markdown]
# ## Setting up AWS Credentials

# %%
import pprint

import boto3

pp = pprint.PrettyPrinter(indent=2)
# %%
# Language Detection
comprehend = boto3.client(service_name="comprehend", region_name="eu-west-1")

# Detect language
text = "This is a test sentence in English"
pp.pprint(comprehend.detect_dominant_language(Text=text))

# %%
# Multi-lingual Language Detection
text = "A: Hallo, wie geht es Ihnen?\nB: Ça va bien. Merci. Et toi?"
pp.pprint(comprehend.detect_dominant_language(Text=text))


# %%
# Sentiment Analysis
text = "Hey, I'm feeling great today!"
print(comprehend.detect_sentiment(Text=text, LanguageCode="en"))

# %%
# Sentiment Analysis
text = (
    "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse "
    "of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way "
    "of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably "
    "a wise long-term inmate named Red."
)
print(comprehend.detect_sentiment(Text=text, LanguageCode="en"))


# %%
# ## Named Entity Recognition
texts = ["Amazon provides web services.", "Jeff is their leader."]
for text in texts:
    print(comprehend.detect_entities(Text=text, LanguageCode="en"))

# %%
# ## Key Phrase Detection
for text in texts:
    print(comprehend.detect_key_phrases(Text=text, LanguageCode="en"))
