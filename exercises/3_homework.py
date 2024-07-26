# %%
# Initialize
import os

import azure.cognitiveservices.speech as speechsdk
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://pythondocinteligence.cognitiveservices.azure.com/"
apikey_document = ""

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(apikey_document)
)

apikey_translator = ""
text_translator = TextTranslationClient(
    credential=AzureKeyCredential(apikey_translator), region="westeurope"
)

apikey_speech = ''
speech_config = speechsdk.SpeechConfig(subscription=apikey_speech,
                                       region='eastus')
audio_config = speechsdk.audio.AudioOutputConfig(filename="outputaudio.wav")
speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=audio_config)

# %%
# Analyze document

document_url = "https://tudasbazis.kulcs-soft.hu/keszletnyilvantarto/wp-content/uploads/pdf/szamla.pdf"
poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-invoice", document_url)
invoices = poller.result()

# %%
# Extract invoice item descriptions

items = invoices.documents[0].fields.get("Items").value
item_descriptions = [
    item.value.get("Description").value for idx, item in enumerate(items)
]

print(item_descriptions)

# %%
# Translate descriptions

responses = text_translator.translate(
    body=list(item_descriptions), from_language="hu", to_language=["en"]
)
translated_item_descriptions = [
    response['translations'][0]['text'] for response in responses]
print(translated_item_descriptions)

# %%
# Text to speech

items_text = " and ".join(translated_item_descriptions)
invoice_items_text = f"Invoice items: {items_text}."
speech_synthesis_result = speech_synthesizer.speak_text_async(invoice_items_text).get()

# %%
# Remove audio file

os.remove("outputaudio.wav")
