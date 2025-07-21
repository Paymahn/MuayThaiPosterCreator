# use this file to initialise the google bucket we use and our connection to it
import os
from dotenv import load_dotenv
from google.cloud import storage
from google.api_core import exceptions

load_dotenv()

class StorageClient:
    def __init__(self):
        self.bucket_name = os.getenv("GCP_BUCKET_NAME")
        if not self.bucket_name:
            raise ValueError("GCP_BUCKET_NAME environment variable not set.")
        self.client = storage.Client()
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





        


        
        
    




