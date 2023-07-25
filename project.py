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
        '--report_xlsx',
        '-r',
        dest='report_xlsx',
        type=str,
        default=None,
        help='Exports the report Excel file'
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
    # Aggregating all User-Input parameters
    options = parser.parse_args()
    
    # Returns: User-Input as the object:  options
    
    # Returns: User-Input as the object:  options
    return options

def interview():
    print("This is an interview.")
    exit()

def main():
    ##  User-Input options
    options = user_input()
    if options.interview is True:
        interview()
        


if __name__ == "__main__":
    main()

