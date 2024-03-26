import json
import csv
from tkinter import Tk, filedialog
import os

# Prompting the user to choose the .json file
root = Tk()
root.withdraw()  # Hide the root window

json_file_path = filedialog.askopenfilename(title="Select a JSON file", filetypes=[("JSON Files", "*.json")])
if not json_file_path:
    print("No file selected. Exiting.")
    exit()

# Reading the JSON content from the chosen file
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Get the keys from the first entry in the JSON data
first_entry = next(iter(json_data.values()))
fieldnames = ['name'] + list(first_entry.keys())

# Preparing the CSV content
csv_data = []
# Extract the required information from the json
for name, info in json_data.items():
    csv_row = {'name': name}
    csv_row.update(info)  # Update the row with the information from the JSON
    csv_data.append(csv_row)

# Get the directory and filename without extension from the JSON file path
directory, json_filename = os.path.split(json_file_path)
csv_filename = os.path.splitext(json_filename)[0] + '.csv'
csv_file_path = os.path.join(directory, csv_filename)

# Now, write the data to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a writer object
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header to the CSV file
    writer.writeheader()

    # Write the rows to the CSV file
    writer.writerows(csv_data)

print(f"The JSON content has been successfully written to the CSV file: {csv_file_path}")
