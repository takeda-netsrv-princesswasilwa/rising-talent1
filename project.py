#!/usr/bin/env python

def user_input() -> object:
    ## Processing command-line parameters
    parser = argparse.ArgumentParser( description='Processing User-Input parameters' )
    parser.add_argument(
        '--pre-check',
        '-l',
        dest='precheck',
        type=str,
        default=None,
        help='Pre-Check Source File! '
    )
    parser.add_argument(
        '--post-check',
        '-r',
        dest='postcheck',
        type=str,
        default=None,
        help='Post-Check Source File! '
    )
    parser.add_argument(
        '--output',
        '-o',
        dest='output',
        type=str,
        default=None,
        help='HTML Output File! '
    )
    parser.add_argument(
        '--width',
        '-w',
        dest='width',
        type=int,
        default='80',
        help='Panels Column Width! '
    )
    parser.add_argument(
        '--verbose',
        '-v',
        const=True,
        default=False,
        dest='verbose',
        nargs='?',
        help='Enable|Disable verbosity'
    )
    ## Aggregating all User-Input parameters
    options = parser.parse_args()
    # if options.verbose:
    #     print( f"\nInput Parameters:\n" )
    #     for option in vars( options ):
    #         print( f"{option} = {getattr( options, option )}" )
    # print()
    # # Returns: <class 'argparse.Namespace'>
    return options

user_input()