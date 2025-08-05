import os
from dotenv import load_dotenv
from internals.cloud_storage import StorageClient

LOCAL_FLAGS_FOLDER = "/Users/paymahn/Downloads/country-flags-main/flags-png"

CLOUD_PATH_FOLDER = "assets/flags"

load_dotenv()
storage = StorageClient()


def upload_flags():
    print(f"Checking for files in: {LOCAL_FLAGS_FOLDER}")

    local_file = os.listdir(LOCAL_FLAGS_FOLDER)
    print(f"Found files: {local_file}")
    for file in local_file:
        if file.endswith(".png"):
            source_path = os.path.join(LOCAL_FLAGS_FOLDER, file)
            destination_path = f"{CLOUD_PATH_FOLDER}/{file}"
            storage.upload_file(source_path, destination_path)
            print(f"uploaded {file}")

if __name__ == "__main__":
    upload_flags()

