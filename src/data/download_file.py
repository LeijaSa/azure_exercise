from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
BLOB_NAME = os.getenv("BLOB_NAME")
DOWNLOAD_FILE_PATH = os.getenv("DOWNLOAD_FILE_PATH")
credential = DefaultAzureCredential()

# Construct the account URL
STORAGE_ACCOUNT_BLOB_URL = os.getenv("STORAGE_ACCOUNT_BLOB_URL")

# Initialize BlobClient
blob_client = BlobClient(
    account_url=STORAGE_ACCOUNT_BLOB_URL,
    container_name=CONTAINER_NAME,
    blob_name=BLOB_NAME,
    credential=credential,
)

# Download the blob
try:
    print(f"Downloading blob '{BLOB_NAME}' from container '{CONTAINER_NAME}'...")
    with open(DOWNLOAD_FILE_PATH, "wb") as download_file:
        blob_data = blob_client.download_blob()
        download_file.write(blob_data.readall())
    print(f"Blob '{BLOB_NAME}' downloaded successfully to '{DOWNLOAD_FILE_PATH}'!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
