# Azure exercises

# Azure Python SDK Exercises

This repository contains a series of exercises demonstrating the use of the **Azure Python SDK** for interacting with Azure services. These exercises are focused on key Azure Storage functionalities, including Blob Storage and Queue Storage.

## **Exercises Overview**

### 1. **Creating an Azure Storage Account**
- Set up an Azure Storage account programmatically using the Azure Python SDK.

### 2. **Blob Storage**
- **Creating a Container**: Learn how to create a blob container in Azure Storage.
- **Uploading a File**: Upload files to a blob container.
- **Downloading a File**: Download files from the blob container for local use.

### 3. **Queue Storage**
- **Creating a Queue**: Create an Azure Queue to store and process messages.
- **Sending Messages**: Programmatically send messages to the queue.
- **Receiving Messages**: Retrieve messages from the queue and process them.

## **Technologies Used**
- **Python**
- **Azure Python SDK**
  - `azure-storage-blob`
  - `azure-storage-queue`
  - `azure-identity`
- **Environment Variables** with `python-dotenv` for secure credential management.

## **Getting Started**
To run the exercises:
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
