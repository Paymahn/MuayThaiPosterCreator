# use this file to initialise the google bucket we use and our connection to it

from dotenv import load_dotenv
load_dotenv()
import os
from google.cloud import storage
from google.api_core import exceptions

load_dotenv()

class StorageClient:
    def __init__(self):
        self.bucket_name = os.getenv("GCP_BUCKET_NAME")
        print(f"--- DEBUG: Reading bucket name as: '{self.bucket_name}'") 
        project_id = os.getenv("GCP_PROJECT_ID")
        if not self.bucket_name or not project_id:
            raise ValueError("GCP_BUCKET_NAME or GCP_PROJECT_ID not set.")
        
        self.client = storage.Client(project=project_id)
        self.bucket = self.client.get_bucket(self.bucket_name)
        print(f"Successfully connected to bucket: {self.bucket.name}")

    def upload_file(self, source_path, destination_path):
        try:
            blob = self.bucket.blob(destination_path)
            blob.upload_from_filename(source_path)
            print(f"File {source_path} uploaded to {destination_path}")
            return True
        except FileNotFoundError: 
            print(f"Error: The source file was not found at {source_path}")
            return False
        except exceptions.GoogleAPICallError as e:
            print(f"An error occurred while uploading to Google Cloud: {e}")
            return False
        
    def download_file(self, source_blob_name, destination_file_path):
        try:
            blob = self.bucket.blob(source_blob_name)
            blob.download_to_filename(destination_file_path)
            print(f"Successfully downloaded {source_blob_name} to {destination_file_path}")
            return True
        except exceptions.NotFound as e:
            print(f"Error: The file {source_blob_name} was not found in the bucket.")
            return False
        except exceptions.GoogleAPICallError as e:
            print(f"An error occurred while downloading from Google Cloud: {e}")
            return False 
        
    def upload_bytes(self, source_bytes, destination_blob_name):
        try:
            blob = self.bucket.blob(destination_blob_name)
            blob.upload_from_string(source_bytes)
            print(f"Successfully uploaded bytes, into {destination_blob_name}")
            return True
        except exceptions.GoogleAPICallError as e:
            print(f"An error occurred while uploading to Google Cloud: {e}")
            return False
        
    def download_bytes(self, source_blob_name: str) -> bytes | None:
        try:
            blob = self.bucket.blob(source_blob_name)
            file_bytes = blob.download_as_bytes()
            print(f"Successfully downloaded {source_blob_name} as bytes.")
            return file_bytes
        except exceptions.NotFound:
            print(f"Error: The file {source_blob_name} was not found in the bucket.")
            return None

        






        


        
        
    




