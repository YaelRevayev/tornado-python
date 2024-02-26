import csv
import json
import constant
import os


def create_dir():
    path = os.path.join(".", constant.DIR_NAME)
    os.mkdir(path)


def csv_to_json(csvFilePath):
    data = {}

    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)
        count_groups = 0
        count_rows = 0
        json_file_name = ""

        for rows in csvReader:
            key = rows[constant.PRIMARY_KEY]
            data[key] = rows
            count_rows += 1

            if count_rows % constant.MAX_RECORDS_PER_FILE == 0:
                count_groups += 1
                write_group_of_records_to_json(data, count_groups)
                data = {}
                count_rows = 0

        if count_rows % constant.MAX_RECORDS_PER_FILE != 0:
            write_group_of_records_to_json(data, count_groups)


def dict_to_json(data, jsonFilePath):
    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def create_serial_json_file(relative_dir, serial):
    path = "./{0}/{1}{2}".format(relative_dir, constant.JSON_FILE_PREFIX, serial)
    open(path, "x")
    return path


def write_group_of_records_to_json(data, count_groups):
    json_file_name = create_serial_json_file(constant.DIR_NAME, count_groups)
    dict_to_json(data, json_file_name)


if __name__ == "__main__":
    create_dir()
    csv_to_json(constant.CSV_SRC_PATH)
