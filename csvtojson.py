import csv
import json
import constant
import os

def create_dir():
    path = os.path.join('.', constant.DIR_NAME) 
    os.mkdir(path) 

def make_json(csvFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        count_groups = 1
        count_rows = 0
        json_file_name=''

        for rows in csvReader:
            key = rows[constant.PRIMARY_KEY]
            data[key] = rows
            count_rows+=1

            if count_rows == 50000:
                count_record_groups+=1
                json_file_name = create_serial_json_file(count_groups)
                records_to_json(data,json_file_name)
                data = {}
                count_rows = 0

        if count_rows % 50000 != 0:
            json_file_name = create_serial_json_file(count_groups)
            records_to_json(data,json_file_name)
                

def records_to_json(data, jsonFilePath):
      with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

def create_serial_json_file(serial):
    return open("./{0}/mada{1}".format(constant.DIR_NAME,serial), "x")

create_dir()
make_json(constant.CSV_SRC_PATH)