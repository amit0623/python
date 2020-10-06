#!/usr/bin/env python3
"""
Author : amitkumar <amitkumar@localhost>
Date   : 2020-10-01
Purpose: Rock the Casbah
"""

import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Implementing Hello ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', '--name',
                        metavar='str',
                        help='Name to Greet',
                        type=str,
                        default='World')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # pos_arg = args.name

    print('Hello, ' + args.name + "!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
