# %%
import pprint

import boto3

pp = pprint.PrettyPrinter(indent=2)

rekognition = boto3.client("rekognition")

# %%

celebrity_response = rekognition.recognize_celebrities(
    Image={
        "S3Object": {
            "Bucket": "amazon-rekognition-example-ceu",
            "Name": "sorosjohn.jpg",
        }
    }
)

pp.pprint(celebrity_response)
# %%

for celebrity in celebrity_response["CelebrityFaces"]:
    print(celebrity["Name"])
    print(celebrity["Urls"])
# %%
