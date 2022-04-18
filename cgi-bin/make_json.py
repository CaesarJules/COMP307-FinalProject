import csv
import json

"""
This function makes a JSON file from a CSV file.
If the JSON file already exists, it is overwritten.
"""
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary and add it to data
        for i in range(len(csvReader)):
            data[i] = csvReader[i]
 
    # write to JSON
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))