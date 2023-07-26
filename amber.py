#!/usr/bin/env python

import argparse
import csv
from csv import reader

def user_input():
    # Command-line parameters
    # Code sourced from Eduardo Valdes
    parser = argparse.ArgumentParser( description='User-Input parameters' )
    parser.add_argument(
        '--interview',
        '-i',
        const=True,
        dest='interview',
        nargs='?',
        help='Calls the interview interface'
    )
    parser.add_argument(
        '--main_csv',
        '-m',
        dest='main_csv',
        type=str,
        default=None,
        help='Imports the main CSV file'
    )
    parser.add_argument(
        '--source_csv',
        '-s',
        dest='source_csv',
        type=str,
        default=None,
        help='Imports the source CSV file'
    )
    parser.add_argument(
        '--report_csv',
        '-r',
        dest='report_csv',
        type=str,
        default=None,
        help='Exports the report Excel file'
    )
    parser.add_argument(
        '--common_column',
        '-c',
        dest='common_column',
        type=str,
        default=None,
        help='Set the common column for data'
    )
    # Aggregating all User-Input parameters
    options = parser.parse_args()
    
    # Returns: User-Input as the object:  options
    return options

def interview():
    print("This is an interview.")
    exit()

def main_csv():
    print("This is going to be the main file.")
    exit()

def source_csv():
    print("This is going to be the source.")
    exit()

def report_csv():
    print("This is going to be the report file.")
    exit()

def common_column():
    print("This is going to be the common column.")
    exit()

def main():
    #  User-Input options
    try:
        api_options = user_input()
        if api_options.interview is True:
            interview()
        if api_options.main_csv is not None:
            main_csv()
        if api_options.source_csv is not None:
            source_csv()
        if api_options.report_csv is not None:
            report_csv()
        if api_options.common_column is not None:
            common_column()
    except Exception as script_error:
        print({"Type": type(script_error), "Error": script_error})

# create a file path for csv files

def load_csv(filename):
    data = list()
    # Open file in read mode
    with open(filename, "r") as file:
        # Reading file using csv.DictReader
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            # Append each row (dictionary) to the data list
            data.append(line)
    return data

if __name__ == "__main__":
    source_filename = "source.csv"
    source_data = load_csv(source_filename)
    print("Source Data:")
    print(source_data)

    main_filename = "main.csv"
    main_data = load_csv(main_filename)
    print("Main Data:")
    print(main_data)

    report_filename = "report.csv"
    report_data = load_csv(report_filename)
    print("Report Data:")
    print(report_data)

    merged_data = source_data + main_data + report_data
    print("Merged Data:")
    print(merged_data)

    main()
