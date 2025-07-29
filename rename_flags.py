from internals.cloud_storage import StorageClient
import os 
from pycountry.db import Country
import pycountry

flags_folder_path = "/Users/paymahn/Downloads/country-flags-main/svg/"
print("Renaming files from two letters to country")

for filename in os.listdir(flags_folder_path):
    if filename.endswith(".svg"):
        two_letter_code: str = filename.split('.')[0]

        country_object : Country = pycountry.countries.get(alpha_2=two_letter_code.upper())
        if country_object:
            old_path = os.path.join(flags_folder_path, filename)
            new_filename = f"{country_object.name}.svg"
            new_path = os.path.join(flags_folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")




