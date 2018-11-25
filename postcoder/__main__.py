#!/usr/bin/env python

import argparse
import sys


def parse_cli():
    """Parse the args"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--postcode")
    parser.add_argument("--country", default="gb")

    args = parser.parse_args()

    for p in ['postcode', 'country']:
        param = eval(p)
        if param in [None, ""]:
            sys.exit("Failed to set {}".format(p))

    return args


def main():
    args = parse_cli()


if __name__ == "__main__":
    main()
