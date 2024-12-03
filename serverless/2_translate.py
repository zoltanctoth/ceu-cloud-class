# %%
# Import required libraries and set up our environment
from pprint import PrettyPrinter

import boto3

print("📚 Setting up the environment...")
pp = PrettyPrinter(indent=2)
translate = boto3.client("translate")
print("✅ Environment setup complete!")
print(f"🌍 Using AWS region: {translate.meta.region_name}")

# %%
# Simple translation from French to English
print("🔄 Translating from French to English...")

french_text = "Bonjour le monde!"
try:
    response = translate.translate_text(Text=french_text, SourceLanguageCode="fr", TargetLanguageCode="en")

    print("\n📝 Translation details:")
    print(f"Original text (French): {french_text}")
    print(f"Translated text (English): {response['TranslatedText']}")

    print("\n📦 Raw response from AWS:")
    pp.pprint(response)
except Exception as e:
    print(f"❌ Error during translation: {str(e)}")

# %%
# Demonstrate auto-detection of source language
print("🔄 Translating with auto-detection...")

spanish_text = "Hola mundo!"
try:
    response = translate.translate_text(Text=spanish_text, SourceLanguageCode="auto", TargetLanguageCode="en")

    print("\n📝 Translation details:")
    print(f"Original text: {spanish_text}")
    print(f"Detected language: {response['SourceLanguageCode']}")
    print(f"Translated text (English): {response['TranslatedText']}")
except Exception as e:
    print(f"❌ Error during translation: {str(e)}")

# %%
# Translate a longer text to demonstrate handling of larger content
print("🔄 Translating longer text to German...")

long_text = (
    "Chronicles the experiences of a formerly successful banker as a prisoner "
    "in the gloomy jailhouse of Shawshank after being found guilty of a crime "
    "he did not commit. The film portrays the man's unique way of dealing "
    "with his new, torturous life; along the way he befriends a number of "
    "fellow prisoners, most notably a wise long-term inmate named Red."
)

try:
    response = translate.translate_text(Text=long_text, SourceLanguageCode="auto", TargetLanguageCode="de")

    print("\n📝 Translation details:")
    print("Original text (English):")
    print("-" * 40)
    print(long_text)
    print("-" * 40)
    print("\nDetected language:", response["SourceLanguageCode"])
    print("\nTranslated text (German):")
    print("-" * 40)
    print(response["TranslatedText"])
    print("-" * 40)

except Exception as e:
    print(f"❌ Error during translation: {str(e)}")

# %%
# Demonstrate formality settings
# Available for specific language pairs
print("👔 Demonstrating formality settings...")

informal_text = "How are you doing?"
try:
    # Formal translation
    formal = translate.translate_text(
        Text=informal_text, SourceLanguageCode="en", TargetLanguageCode="de", Settings={"Formality": "FORMAL"}
    )

    # Informal translation
    informal = translate.translate_text(
        Text=informal_text, SourceLanguageCode="en", TargetLanguageCode="de", Settings={"Formality": "INFORMAL"}
    )

    print("\n📝 Formality comparison:")
    print(f"Original: {informal_text}")
    print(f"Formal translation: {formal['TranslatedText']}")
    print(f"Informal translation: {informal['TranslatedText']}")

except Exception as e:
    print(f"❌ Error: {str(e)}")


# %%
# The following cells are provided only for your reference in case you want to use them in the assignment

# %%
# Demonstrate translation with terminology
# Custom terminology helps maintain consistent translations for specific terms
import os

print("📚 Using custom terminology...")

try:
    # First, create a custom terminology file
    terminology = {
        "file": "custom-terms.csv",
        "content": "en,de\ncloud computing,Cloudcomputing\nartificial intelligence,Künstliche Intelligenz",
    }

    with open(terminology["file"], "w") as f:
        f.write(terminology["content"])

    # Import the terminology
    with open(terminology["file"], "rb") as f:
        response = translate.import_terminology(
            Name="tech-terms", MergeStrategy="OVERWRITE", TerminologyData={"File": f.read(), "Format": "CSV"}
        )
    print("✅ Custom terminology imported")

    # Use the terminology in translation
    text = "We specialize in cloud computing and artificial intelligence solutions."
    response = translate.translate_text(
        Text=text, TerminologyNames=["tech-terms"], SourceLanguageCode="en", TargetLanguageCode="de"
    )

    print("\n📝 Translation with custom terminology:")
    print(f"Original: {text}")
    print(f"Translated: {response['TranslatedText']}")

except Exception as e:
    print(f"❌ Error: {str(e)}")
finally:
    # Clean up
    if os.path.exists(terminology["file"]):
        os.remove(terminology["file"])

# %%
