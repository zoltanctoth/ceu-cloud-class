# %%
# Import required libraries and set up our environment
import pprint

import boto3

print("📚 Setting up the environment...")

# Initialize pretty printer for better output formatting
pp = pprint.PrettyPrinter(indent=2)

# Create Comprehend client
comprehend = boto3.client(service_name="comprehend", region_name="eu-west-1")

print("✅ Environment setup complete!")
print(f"🌍 Using AWS region: {comprehend.meta.region_name}")

# %%
# Demonstrate simple language detection
print("🔍 Testing single-language detection...")

text = "This is a test sentence in English"
try:
    response = comprehend.detect_dominant_language(Text=text)

    print("\n📝 Input text:")
    print(f'"{text}"')

    print("\n🌐 Detected languages:")
    for language in response["Languages"]:
        print(f"- {language['LanguageCode']}: {language['Score']:.2%} confidence")

    print("\n📦 Raw response:")
    pp.pprint(response)
except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Demonstrate multi-language detection
print("🔍 Testing multi-language detection...")

multilingual_text = "A: Hallo, wie geht es Ihnen?\nB: Ça va bien. Merci. Et toi?"
try:
    response = comprehend.detect_dominant_language(Text=multilingual_text)

    print("\n📝 Input text:")
    print(f'"{multilingual_text}"')

    print("\n🌐 Detected languages:")
    for language in response["Languages"]:
        print(f"- {language['LanguageCode']}: {language['Score']:.2%} confidence")

except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Demonstrate simple sentiment analysis
print("� Testing sentiment analysis with short text...")

text = "Hey, I'm feeling great today!"
try:
    response = comprehend.detect_sentiment(Text=text, LanguageCode="en")

    print("\n📝 Input text:")
    print(f'"{text}"')

    print("\n💭 Sentiment analysis:")
    print(f"Overall sentiment: {response['Sentiment']}")
    print("\nSentiment scores:")
    for sentiment, score in response["SentimentScore"].items():
        print(f"- {sentiment}: {score:.2%}")

except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Demonstrate sentiment analysis with longer text
print("😊 Testing sentiment analysis with longer text...")

long_text = (
    "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse "
    "of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way "
    "of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably "
    "a wise long-term inmate named Red."
)

try:
    response = comprehend.detect_sentiment(Text=long_text, LanguageCode="en")

    print("\n📝 Input text:")
    print("-" * 40)
    print(long_text)
    print("-" * 40)

    print("\n💭 Sentiment analysis:")
    print(f"Overall sentiment: {response['Sentiment']}")
    print("\nSentiment scores:")
    for sentiment, score in response["SentimentScore"].items():
        print(f"- {sentiment}: {score:.2%}")

except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Demonstrate entity recognition
print("🏷️  Testing named entity recognition...")

texts = [
    "Welcome to CEU's Data Engineering course run by Zoltan Toth.",
    "Here we learn about the internet, AWS and Data Engineering.",
]

try:
    print("\n🔍 Analyzing entities in texts:")

    for i, text in enumerate(texts, 1):
        print(f'\n📝 Text {i}: "{text}"')
        response = comprehend.detect_entities(Text=text, LanguageCode="en")

        if response["Entities"]:
            print("Found entities:")
            for entity in response["Entities"]:
                print(f"- {entity['Text']} ({entity['Type']}): {entity['Score']:.2%} confidence")
        else:
            print("No entities found.")

except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
# Demonstrate key phrase detection
print("🔑 Testing key phrase detection...")

try:
    print("\n🔍 Analyzing key phrases in texts:")

    for i, text in enumerate(texts, 1):
        print(f'\n📝 Text {i}: "{text}"')
        response = comprehend.detect_key_phrases(Text=text, LanguageCode="en")

        if response["KeyPhrases"]:
            print("Found key phrases:")
            for phrase in response["KeyPhrases"]:
                print(f"- {phrase['Text']}: {phrase['Score']:.2%} confidence")
        else:
            print("No key phrases found.")

        print("\n📦 Raw response:")
        pp.pprint(response)
except Exception as e:
    print(f"❌ Error: {str(e)}")

# %%
