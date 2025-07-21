print("Attempting to import StorageClient...")

try:
    from internals.cloud_storage import StorageClient
    print("✅ Success: The import is correct.")

except ImportError as e:
    print(f"❌ Error: The import failed. Python could not find the module. Details: {e}")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")