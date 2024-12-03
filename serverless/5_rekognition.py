# %%
# Import required libraries and set up our environment
import pprint

import boto3

print("📚 Setting up the environment...")

# Initialize pretty printer for better output formatting
pp = pprint.PrettyPrinter(indent=2)

# Create Rekognition client
rekognition = boto3.client("rekognition")

print("✅ Environment setup complete!")
print(f"🌍 Using AWS region: {rekognition.meta.region_name}")

# %%
# Analyze image for celebrity detection
print("🔍 Analyzing image for celebrities...")

S3_BUCKET = "de2-datasets"
S3_KEY = "soros.jpg"

print("\n📂 Image location:")
print(f"- Bucket: {S3_BUCKET}")
print(f"- Key: {S3_KEY}")

try:
    celebrity_response = rekognition.recognize_celebrities(
        Image={
            "S3Object": {
                "Bucket": S3_BUCKET,
                "Name": S3_KEY,
            }
        }
    )

    print("\n✅ Image analysis complete!")
    print(f"Found {len(celebrity_response['CelebrityFaces'])} celebrities")

    print("\n📦 Raw response from AWS:")
    pp.pprint(celebrity_response)

except Exception as e:
    print(f"❌ Error analyzing image: {str(e)}")

# %%
# Process and display celebrity information
print("👥 Celebrity Information:")

try:
    if not celebrity_response["CelebrityFaces"]:
        print("No celebrities detected in the image.")
    else:
        for i, celebrity in enumerate(celebrity_response["CelebrityFaces"], 1):
            print(f"\n🌟 Celebrity {i}:")
            print(f"Name: {celebrity['Name']}")
            print(f"Confidence: {celebrity['MatchConfidence']:.2f}%")
            print("\nReference URLs:")
            for url in celebrity["Urls"]:
                print(f"- https://{url}")

            # Print face details if available
            if "Face" in celebrity:
                print("\nFace Details:")
                face = celebrity["Face"]
                emotions = face.get("Emotions", [])
                if emotions:
                    top_emotion = emotions[0]  # Emotions are returned sorted by confidence
                    print(f"- Top emotion: {top_emotion['Type']} ({top_emotion['Confidence']:.1f}%)")

            print("-" * 40)

except Exception as e:
    print(f"❌ Error processing results: {str(e)}")

print("\nℹ️  Note: Celebrity recognition accuracy may vary based on image quality and database coverage")

# %%
