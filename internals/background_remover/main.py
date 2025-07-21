from cloudevents.http import CloudEvent
import functions_framework
from internals.cloud_storage import StorageClient

@functions_framework.cloud_event
def remove_background(cloud_event : CloudEvent):
    attributes = cloud_event.get_attributes()
    bucket_name = attributes["bucket"]
    file_name = attributes["name"]
    if not file_name.startswith("inputs/"):
        print(f"Ignoring file {file_name} as it was not in the inputs/ folder.")
        return
    
    storage = StorageClient()
  



