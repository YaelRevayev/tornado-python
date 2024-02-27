import csv
import constant
import os


def extract_records_from_csv_to_list(csvFilePath):
    if not os.path.exists(csvFilePath):
        raise Exception("Cant find given source path")

    list = []

    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            list.append(rows)

    return list
