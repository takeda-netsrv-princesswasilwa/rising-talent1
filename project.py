#!/usr/bin/env python

import argparse
import re

def user_input():
    """Command-line parameters"""
    # user_input sourced from Eduardo Valdes
    parser = argparse.ArgumentParser( description='User-Input parameters' )
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
        nargs='+',
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
    
    # Returns: User-Input as the object: options
    return options

def interview():
    """Requests manual input"""
    main_csv_path = input("Enter main CSV path: ")
    main_csv_path_final = main_csv(main_csv_path, True)
    
    source_csv_path = input("Enter source CSV path: ")
    source_csv_path_final = source_csv(source_csv_path, True)

    report_xlsx_path = input("Enter report XLSX path: ")
    report_xlsx_path_final = report_xlsx(report_xlsx_path, True)

    search_column = input("Enter common column: ")
    
    return main_csv_path_final, source_csv_path_final, report_xlsx_path_final, search_column

def file_validation(file_checked, file_which_checked,file_type_checked, file_wrong = "."):
    """Ensures proper file input format"""
    while re.match(rf"\w*(.{file_type_checked})$", file_checked.lower()) is None:
        print(f"Improper file{file_wrong} Format: *.{file_type_checked}")
        file_checked = input(f"Enter {file_which_checked} {file_type_checked.upper()} path: ")
    return file_checked

# First input is file path,
# Second input is main, source or report,
# Third input is .csv or .xlsx,
# Fourth input flags if an interview is required.

# If interview flag does not exist create an item list,
# and if file path is a list confirm file type matches, append new list and return new list,
# or if file path is not a list confirm file type matches and return file path.

# Else if interview flag does exist,
# Continue requesting file path until valid file path is provided and return file path.

def input_parser(file_path_parser, file_which, file_type, interview_request_final):
    """Returns list of file paths"""
    if interview_request_final is False:
        item_list = []
        if type(file_path_parser) is list:
            for item in file_path_parser:
                if re.match(rf"\w*(.{file_type})$", item.lower()) is not None:
                    item_list.append(item)
                item_list.append(file_validation(item, file_which, file_type, f": {item}."))
            return item_list
        if re.match(rf"\w*(.{file_type})$", file_path_parser.lower()) is not None:
            return file_path_parser
        file_path_parser = file_validation(file_path_parser, file_which, file_type)
        return file_path_parser
    else:
        file_path_parser = file_validation(file_path_parser, file_which, file_type)
        return file_path_parser

def main_csv(file_path,interview_request = False):
    """Returns main_csv file when called"""
    return input_parser(file_path, "main", "csv", interview_request)

def source_csv(file_path,interview_request = False):
    """Returns source_csv files when called"""
    return input_parser(file_path, "source", "csv", interview_request)

def report_xlsx(file_path,interview_request = False):
    """Returns report_xlsx file when called"""
    return input_parser(file_path, "report", "xlsx", interview_request)

def common_column(search_column):
    """Returns common_column when called"""
    return search_column

def main():
    """Calls user_input and returns result"""
    try:
        api_options = user_input()
        if api_options.main_csv and api_options.source_csv and api_options.report_xlsx and api_options.common_column is not None:
            output_list = []
            output_list.append(main_csv(api_options.main_csv))
            output_list.append(source_csv(api_options.source_csv))
            output_list.append(report_xlsx(api_options.report_xlsx))
            output_list.append(common_column(api_options.common_column))
            print(output_list)
        else:
            print(list(interview()))
    except Exception as script_error:
        print({"Type": type(script_error), "Error": script_error})

if __name__ == "__main__":
    # This should be deleted
    print("This is a test.")
    # Delete prior
    main()
