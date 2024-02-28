import os_operations
from extract import extract
from load import load
import constant

def main():
    records = extract(constant.CSV_SRC_PATH)

    os_operations.create_dir(constant.DIR_NAME)
    
    load(records, "./{}".format(constant.DIR_NAME))


if __name__ == "__main__":
    main()
