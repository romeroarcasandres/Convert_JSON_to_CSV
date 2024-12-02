# Convert_JSON_to_CSV
It converts a .json file into a .csv file

## Overview:
This script converts JSON files into CSV format. It prompts the user to select a JSON file using a file dialog, reads the JSON content, and then converts it into CSV format. The resulting CSV file contains data extracted from the JSON, with each JSON object becoming a row in the CSV file.

## Requirements:
Python 3
tkinter library (utilized for file dialog)
csv library (for CSV handling)
json library (for JSON handling)
os library (for file path operations)

## Files
JSON_to_CSV_Converter.py

## Usage
1. Run the script.
2. A file dialog will prompt you to select a JSON file.
3. After selecting the JSON file, the script will read its content and convert it into CSV format.
4. The resulting CSV file will be saved in the same directory as the selected JSON file with the same name but with a ".csv" extension.

See "JSON_to_CSV_Converter_1.JPG" and "JSON_to_CSV_Converter_2.JPG".

## Important Note
Ensure that the selected file is a valid JSON file.
The script assumes that the JSON file contains objects with consistent keys across entries.
The CSV file will have a header row derived from the keys of the first JSON entry.
Unicode encoding (utf-8) is used for reading and writing files to handle diverse character sets.

## License
This project is governed by the CC BY-NC 4.0 license. For comprehensive details, kindly refer to the LICENSE file included with this project.
