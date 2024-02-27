import os_operations
import extract_from_csv as extract_from_csv
import load
import constant

def main():
    records = extract_from_csv.extract_records_from_csv_to_list(constant.CSV_SRC_PATH)

    os_operations.create_dir(constant.DIR_NAME)

    list_of_dicts = load.grouping_records_from_list(
        records, constant.MAX_RECORDS_PER_FILE
    )

    load.write_dict_to_json_file(list_of_dicts, "./{}".format(constant.DIR_NAME))


if __name__ == "__main__":
    main()
