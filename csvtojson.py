import csv
import json
import constant

def make_json(csvFilePath):
     
    data = {}
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        count_record_groups = 0
        count_rows = 0
        json_file_name=''

        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows[constant.PRIMARY_KEY]
            data[key] = rows
            count_rows+=1
            if count_rows == 50000:
                records_to_json(data,json_file_name)
                

def records_to_json(d):
    pass

def generate_serial_json_file():
    pass
# Call the make_json function
make_json(constant.CSV_SRC_PATH)