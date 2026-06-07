import os
import shutil

source_folder = "files"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = file.split(".")[-1]

        folder_name = extension.upper() + "_Files"
        folder_path = os.path.join(source_folder, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(file_path, os.path.join(folder_path, file))

print("Files organized successfully!")