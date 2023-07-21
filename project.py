#!/usr/bin/env python

import argparse

def user_input() -> object:
    ## Processing command-line parameters
    parser = argparse.ArgumentParser( description='Processing User-Input parameters' )
    parser.add_argument(
        '--interview',
        '-i',
        const=False,
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
        help='Exports the report CSV file'
    )
    parser.add_argument(
        '--common_column',
        '-c',
        dest='common_column',
        type=str,
        default=None,
        help='Set the common column for data'
    )
    return parser.parse_args()

# compare main with sources

# merge files to dictionary
def merge_sources():
    main()


def interview():
    print("This is an interview.")
    exit()

def main():
    ##  User-Input options
    options = user_input()
    if options.interview == True:
        interview()
        


if __name__ == "__main__":
    main()