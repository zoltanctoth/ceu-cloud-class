# %%
# Import
import os
import uuid

from azure.storage.blob import BlobServiceClient
from azure.identity import AzureCliCredential

blob_service_client = BlobServiceClient(
    "https://pythonailearn.blob.core.windows.net", credential=AzureCliCredential())

# %%
# List containers
containers = blob_service_client.list_containers()
for container in containers:
    print(container.name)

# %%
# Create container
container_name = str(uuid.uuid4())
container_client = blob_service_client.create_container(container_name)
print(f"Container created: {container_name}")

# %%
# Create sample file
file_name = "my_content.txt"
with open(file=file_name, mode='w') as file:
    file.write("text")

# %%
# Upload blob
with open(file=file_name, mode='rb') as file:
    container_client.upload_blob(name=file_name, data=file)
    print(f"File uploaded to container: {file_name}")

# %%
# Download
downloaded_file_name = 'my_content_downloaded.txt'
with open(file=downloaded_file_name, mode="wb") as download_file:
    download_file.write(container_client.download_blob(file_name).readall())
print(f"File downloaded from container: {downloaded_file_name}")

# %%
# Display file contents
with open(downloaded_file_name, "r") as file:
    content = file.read()
    print(f"Content: {content}")

# %%
# Delete blob:
container_client.delete_blob(file_name)
print("Delete blob")

# %%
# Delete container
container_client.delete_container()
print("Delete container")

# %%
# Delete files
os.remove(file_name)
os.remove(downloaded_file_name)
print("Delete files")
