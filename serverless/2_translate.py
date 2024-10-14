# %%
# Import required libraries
import boto3

# Initialize the Amazon Translate client
translate = boto3.client("translate")

# %%
# Translate text from French to English
response = translate.translate_text(Text="Bonjour le monde!", SourceLanguageCode="fr", TargetLanguageCode="en")
print(response["TranslatedText"])

# %%
# Translate text from Spanish to English (auto-detect source language)
response = translate.translate_text(Text="Hola mundo!", SourceLanguageCode="auto", TargetLanguageCode="en")
print(response["TranslatedText"])

# %%
# Translate text to German (auto-detect source language)
long_text = (
    "Chronicles the experiences of a formerly successful banker as a prisoner "
    "in the gloomy jailhouse of Shawshank after being found guilty of a crime "
    "he did not commit. The film portrays the man's unique way of dealing "
    "with his new, torturous life; along the way he befriends a number of "
    "fellow prisoners, most notably a wise long-term inmate named Red."
)
response = translate.translate_text(Text=long_text, SourceLanguageCode="auto", TargetLanguageCode="de")
print(response["TranslatedText"])
