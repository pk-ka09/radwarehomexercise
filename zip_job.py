import os
import sys
import zipfile

# Create an array of letters
letters = [chr(ord('a') + i) for i in range(26)]

# Create txt files
txt_files_created = []
for letter in letters:
    txt_filename = f"{letter}.txt"
    with open(txt_filename, "w") as txt_file:
        txt_files_created.append(txt_filename)

# Check if all txt files were created
if len(txt_files_created) != 26:
    print("Error: Not all txt files were created")
    sys.exit(1)
else:
    print("All txt files created successfully")

# Create zip files
zip_files_created = []
for letter in letters:
    txt_filename = f"{letter}.txt"
    zip_filename = f"{letter}_{os.environ['VERSION']}.zip"
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        zip_file.write(txt_filename)
        zip_files_created.append(zip_filename)

# Check if all zip files were created
if len(zip_files_created) != 26:
    print("Error: Not all zip files were created")
    sys.exit(1)
else:
    print("All zip files created successfully")
