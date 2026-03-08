#!/usr/bin/env python3
"""
module to convert csv data to json format
"""

import csv
import json



def convert_csv_to_json(csv_filename):
    """
    convert s csv file to a json file named data.json

    args:
        csv_filename (str): Name of th ecsv file

    reeturns:
        bool: true if conversion was succesful, false otherwise.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader: csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, OSError, csv.Error):
        return False
