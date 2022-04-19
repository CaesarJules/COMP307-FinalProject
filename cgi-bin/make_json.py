import csv, json

"""
This function makes a JSON file from a CSV file.
If the JSON file already exists, it is overwritten.
"""
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {"data": []}
        
    # Open a csv reader called DictReader
    with open(csvFilePath, 'r') as csvf:
        csvReader = csv.DictReader(csvf)    
        # Convert each row into a dictionary and add it to data
        for row in csvReader:
            data["data"].append(row)

    # write to JSON
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))