from azure.storage.queue import QueueServiceClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
QUEUE_NAME = os.getenv("QUEUE_NAME") 
credential = DefaultAzureCredential()

# Construct the account URL
STORAGE_ACCOUNT_URL = os.getenv("STORAGE_ACCOUNT_URL")

# Authenticate and initialize the QueueServiceClient
queue_service_client = QueueServiceClient(
    account_url=STORAGE_ACCOUNT_URL,
    credential=credential
)

# Create the queue
try:
    print(f"Creating queue '{QUEUE_NAME}'...")
    queue_client = queue_service_client.create_queue(QUEUE_NAME)
    print(f"Queue '{QUEUE_NAME}' created successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
