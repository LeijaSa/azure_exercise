from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
BLOB_NAME = os.getenv("BLOB_NAME")
LOCAL_FILE_PATH = os.getenv("LOCAL_FILE_PATH")
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

# Upload the file
try:
    with open(LOCAL_FILE_PATH, "rb") as data:
        print(f"Uploading file '{LOCAL_FILE_PATH}' to container '{CONTAINER_NAME}'...")
        blob_client.upload_blob(data, overwrite=True)  # Overwrite=True allows replacing existing blobs
        print(f"File '{BLOB_NAME}' uploaded successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
