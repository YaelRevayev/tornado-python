import os_operations
import extract as extract
import load
import constant

def main():
    records = extract.extract_csv(constant.CSV_SRC_PATH)

    os_operations.create_dir(constant.DIR_NAME)
    
    load.write_json(records, "./{}".format(constant.DIR_NAME))


if __name__ == "__main__":
    main()
