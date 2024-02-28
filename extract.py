import csv

def extract(csvFilePath):
    try:
        list = []

        with open(csvFilePath, encoding="utf-8") as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                list.append(rows)

        return list
    except NameError:
        print(NameError)

