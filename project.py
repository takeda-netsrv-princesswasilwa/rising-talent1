#!/usr/bin/env python

import argparse
import re


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


def interview():
    main_csv_path = input("Enter main CSV path: ")
    main_csv_path_final = main_csv(main_csv_path, True)
    
    source_csv_path = input("Enter source CSV path: ")
    source_csv_path_final = source_csv(source_csv_path, True)
    
    report_xlsx_path = input("Enter report XLSX path: ")
    report_xlsx_path_final = report_xlsx(report_xlsx_path, True)
    
    search_column = input("Enter common column: ")
    
    return main_csv_path_final, source_csv_path_final, report_xlsx_path_final, search_column

def input_parser(file_path, file_which, file_type, file_spelled, file_api, interview_request_final):
    if interview_request_final is False:
        return file_api
    else:
        while re.match(rf"\w*(.{file_type})$", file_path.lower()) is None:
            print(f"Improper file. Format: *.{file_type}")
            file_path = input(f"Enter {file_which} {file_spelled} path: ")
            return file_path

def main_csv(file_path,interview_request = False):
    input_parser(file_path, "main", "csv", "CSV", api_options.main_csv, interview_request)

def source_csv(file_path,interview_request = False):
    input_parser(file_path, "source", "csv", "CSV", api_options.source_csv, interview_request)

def report_xlsx(file_path,interview_request = False):
    input_parser(file_path, "report", "xslx", "XSLX", api_options.main_csv, interview_request)

# Returns common_column when called
def common_column(interview_request = False):
    search_column = api_options.common_column
    return search_column

def main():
    #  User-Input options
    global api_options
    try:
        api_options = user_input()
        if api_options.interview is True:
            print(interview())
        if api_options.main_csv is not None:
            main_csv()
        if api_options.source_csv is not None:
            source_csv()
        if api_options.report_xlsx is not None:
            report_xlsx()
        if api_options.common_column is not None:
            common_column()
    except Exception as script_error:
        print({"Type": type(script_error), "Error": script_error})

if __name__ == "__main__":
    main()
