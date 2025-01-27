from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku, Kind
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace these with your Azure details
SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")
RESOURCE_GROUP_NAME = os.getenv("RESOURCE_GROUP_NAME")
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
LOCATION = "eastus"  # Example: "eastus", "westus", etc.

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()
storage_client = StorageManagementClient(credential, SUBSCRIPTION_ID)

# Define storage account parameters
params = StorageAccountCreateParameters(
    sku=Sku(name="Standard_LRS"),  # Storage account SKU (Standard_LRS, Premium_LRS, etc.)
    kind=Kind.STORAGE_V2,         # Kind of storage account (Storage, StorageV2, BlobStorage, etc.)
    location=LOCATION,            # Azure region
    enable_https_traffic_only=True  # Enforce HTTPS
)

# Create the storage account
print(f"Creating storage account '{STORAGE_ACCOUNT_NAME}' in resource group '{RESOURCE_GROUP_NAME}'...")
poller = storage_client.storage_accounts.begin_create(
    resource_group_name=RESOURCE_GROUP_NAME,
    account_name=STORAGE_ACCOUNT_NAME,
    parameters=params
)
storage_account = poller.result()  # Wait for the operation to complete
print(f"Storage account '{STORAGE_ACCOUNT_NAME}' created successfully!")
