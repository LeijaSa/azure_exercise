from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ResourceExistsError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
credential = DefaultAzureCredential()

# Construct the account URL
STORAGE_ACCOUNT_BLOB_URL = os.getenv("STORAGE_ACCOUNT_BLOB_URL")

# Authenticate and initialize the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=STORAGE_ACCOUNT_BLOB_URL, credential=credential)

# Create the container if it doesn't already exist
try:
    print(f"Creating container '{CONTAINER_NAME}'...")
    container_client = blob_service_client.create_container(CONTAINER_NAME)
    print(f"Container '{CONTAINER_NAME}' created successfully!")
except ResourceExistsError:
    print('A container with this name already exists')
except Exception as ex:
    print(f"Another error occurred: {str(ex)}")
