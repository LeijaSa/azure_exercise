
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
QUEUE_NAME = os.getenv("QUEUE_NAME")
MESSAGE = "Hello there again!"  # The message
credential = DefaultAzureCredential()

# Construct the account URL
STORAGE_ACCOUNT_URL = os.getenv("STORAGE_ACCOUNT_URL")


connect_str = os.getenv("CONNECT_STR")
queue_client = QueueClient.from_connection_string(connect_str, QUEUE_NAME)


# Send the message
try:
    print(f"Sending message to queue '{QUEUE_NAME}'...")
    queue_client.send_message(MESSAGE)
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
