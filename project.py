#!/usr/bin/env python

import argparse
import re
import sys


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
        '--report_xlsx',
        '-r',
        dest='report_xlsx',
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

# Requests manual input
def interview():
    main_csv_path = input("Enter main CSV path: ")
    main_csv_path_final = main_csv(main_csv_path, True)
    
    source_csv_path = input("Enter source CSV path: ")
    source_csv_path_final = source_csv(source_csv_path, True)

    report_xlsx_path = input("Enter report XLSX path: ")
    report_xlsx_path_final = report_xlsx(report_xlsx_path, True)

    search_column = input("Enter common column: ")
    
    return main_csv_path_final, source_csv_path_final, report_xlsx_path_final, search_column

# Parses input
def input_parser(file_path_parser, file_which, file_type, file_api, interview_request_final):
    if interview_request_final is False:
        return file_path_parser
    else:
        while re.match(rf"\w*(.{file_type})$", file_path_parser.lower()) is None:
            print(f"Improper file. Format: *.{file_type}")
            file_path_parser = input(f"Enter {file_which} {file_type.upper()} path: ")
        return file_path_parser

def main_csv(file_path,interview_request = False):
    return input_parser(file_path, "main", "csv", api_options.main_csv, interview_request)

def source_csv(file_path,interview_request = False):
    return input_parser(file_path, "source", "csv", api_options.source_csv, interview_request)

def report_xlsx(file_path,interview_request = False):
    return input_parser(file_path, "report", "xlsx", api_options.report_xlsx, interview_request)

# Returns common_column when called
def common_column(interview_request = False):
    search_column = api_options.common_column
    return search_column

def main():
    #  User-Input options
    global api_options
    try:
        api_options = user_input()
        if api_options.main_csv is not None:
            print(main_csv(sys.argv[1:]))
        else:
            print(interview())
    except Exception as script_error:
        print({"Type": type(script_error), "Error": script_error})

if __name__ == "__main__":
    main()
