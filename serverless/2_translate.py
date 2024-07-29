# %%
# Import
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential

# %%
# Initialize client
apikey = ""
text_translator = TextTranslationClient(
    credential=AzureKeyCredential(apikey), region="westeurope"
)

# %%
# Translate text from French to English
response = text_translator.translate(
    body=["Bonjour le monde!"], from_language="fr", to_language=["en"]
)
print(response[0]["translations"][0]["text"])

# %%
# Translate text from Spanish to English (auto-detect source language)
response = text_translator.translate(body=["Hola mundo!"], to_language=["en"])
print(response[0]["translations"][0]["text"])

# %%
# Translate text to German (auto-detect source language)
long_text = (
    "Chronicles the experiences of a formerly successful banker as a prisoner "
    "in the gloomy jailhouse of Shawshank after being found guilty of a crime "
    "he did not commit. The film portrays the man's unique way of dealing "
    "with his new, torturous life; along the way he befriends a number of "
    "fellow prisoners, most notably a wise long-term inmate named Red."
)

response = text_translator.translate(body=[long_text], to_language=["de"])
print(response[0]["translations"][0]["text"])
