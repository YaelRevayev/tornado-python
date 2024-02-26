import csv
import json
import constant
import os


def create_dir(dir_name):
    path = os.path.join(".", dir_name)
    os.makedirs(path, exist_ok=True)


def csv_to_json(csvFilePath):
    data = {}

    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)
        count_groups = 0
        count_rows = 0

        for rows in csvReader:
            key = rows[constant.PRIMARY_KEY]
            data[key] = rows
            count_rows += 1

            if count_rows % constant.MAX_RECORDS_PER_FILE == 0:
                count_groups += 1
                write_dict_to_json(data, count_groups, constant.DIR_NAME)
                data = {}
                count_rows = 0

        if count_rows % constant.MAX_RECORDS_PER_FILE != 0:
            write_dict_to_json(data, count_groups, constant.DIR_NAME)


def write_dict_to_json(data, count_groups, dir_path):
    path = "./{0}/{1}{2}".format(dir_path, constant.JSON_FILE_PREFIX, count_groups)
    file = open(path, "x")

    with open(path, "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    file.close()


if __name__ == "__main__":
    create_dir(constant.DIR_NAME)
    csv_to_json(constant.CSV_SRC_PATH)
