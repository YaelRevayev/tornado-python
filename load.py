import constant
import os
import json
from os_operations import create_dir


def write_dict_to_json_file(list_of_dicts, dest_dir_path):
    serial_identifier = 0
    for data in list_of_dicts:

        path = "./{0}/{1}{2}".format(
            dest_dir_path, constant.JSON_FILE_PREFIX, serial_identifier
        )

        if os.path.exists(path):
            return None

        file = open(path, "x")

        with open(path, "w", encoding="utf-8") as jsonf:
            jsonf.write(json.dumps(data, indent=4))
        serial_identifier += 1

        file.close()


def grouping_records_from_list(list_of_records, max_records_per_file):
    data = {}
    count_rows = 0
    list = []

    for row in list_of_records:
        key = row[constant.PRIMARY_KEY]
        data[key] = row
        count_rows += 1

        if count_rows % max_records_per_file == 0:
            list.append(data)
            data = {}
            count_rows = 0

    if count_rows % max_records_per_file != 0:
        list.append(data)

    return list
