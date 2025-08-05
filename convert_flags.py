import os
from internals.cloud_storage import StorageClient
import cairosvg

flags_folder = "/Users/paymahn/Downloads/country-flags-main/svg"


for filename in os.listdir(flags_folder):
    if filename.endswith(".svg"):
        source_path = os.path.join(flags_folder, filename)
        new_filename = filename.replace(".svg", ".png")
        destination_path = os.path.join(flags_folder, new_filename)
        try:
            cairosvg.svg2png(url=source_path, write_to=destination_path)
            print(f"  > Converted {filename} to {new_filename}")
        except Exception as e:
            print(f"  > FAILED to convert {filename}: {e}")

print("Conversion complete.")

