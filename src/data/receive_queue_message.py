from azure.storage.queue import QueueClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
QUEUE_NAME = os.getenv("QUEUE_NAME")
MAX_MESSAGES = 1  # Number of messages to retrieve (up to 32 messages at once)
credential = DefaultAzureCredential()

# Construct the account URL
STORAGE_ACCOUNT_URL = os.getenv("STORAGE_ACCOUNT_URL")

connect_str = os.getenv("CONNECT_STR")
queue_client = QueueClient.from_connection_string(connect_str, QUEUE_NAME)

# Receive a message
try:
    print(f"Receiving message from queue '{QUEUE_NAME}'...")
    
    # Receive messages from the queue (up to MAX_MESSAGES at a time)
    messages = queue_client.receive_messages(max_messages=MAX_MESSAGES)

    for message in messages:
        print(f"Received message: {message.content}")
        
        # After processing, delete the message from the queue
        queue_client.delete_message(message)
        print(f"Message deleted from queue.")
    
    if not messages:
        print("No messages in the queue.")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
