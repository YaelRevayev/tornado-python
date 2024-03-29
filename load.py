import constant
import os
import json


def load(list_of_records, dest_dir_path,max_records_per_file = constant.MAX_RECORDS_PER_FILE):
    list_of_dicts = grouping_records_from_list(list_of_records)
    serial_identifier = len(os.listdir(dest_dir_path)) + 1

    for data in list_of_dicts:
        path = "./{0}/{1}{2}".format(
        dest_dir_path, constant.JSON_FILE_PREFIX, serial_identifier
            )

        with open(path, "w+", encoding="utf-8") as jsonf:
               jsonf.write(json.dumps(data, indent=4))
        serial_identifier += 1


def grouping_records_from_list(list_of_records):
    data = {}
    count_rows = 0
    list = []

    for row in list_of_records:
        key = row[constant.PRIMARY_KEY]
        data[key] = row
        count_rows += 1

        if count_rows % constant.MAX_RECORDS_PER_FILE == 0:
            list.append(data)
            data = {}
            count_rows = 0

    if count_rows % constant.MAX_RECORDS_PER_FILE != 0:
        list.append(data)

    return list