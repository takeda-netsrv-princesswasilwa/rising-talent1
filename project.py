#!/usr/bin/env python

import argparse


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
    main_csv_path = api_options.main_csv
    return main_csv_path
    exit()

def source_csv():
    source_csv_path = api_options.source_csv
    return source_csv_path
    exit()

def report_csv():
    report_csv_path = api_options.report_csv
    return report_csv_path
    exit()

# Returns common_column when called
def common_column():
    search_column = api_options.common_column
    return search_column
    exit()

def main():
    #  User-Input options
    global api_options
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

if __name__ == "__main__":
    main()
