# -*- coding: utf-8 -*-

__author__ = 'carlosp420'

import argparse


def create_parser():
    description = "Take a FASTA file and generate alignments based on gene and consensus sequences for same gene and same individual."
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     )
    parser.add_argument('-i', '--input', action='store', help='input Fasta filename',
                        required=True, dest='fasta_file',
                        )
    return parser


def get_started(args):
    print(args)


def main():
    parser = create_parser()
    args = parser.parse_args()
    get_started(args)


if __name__ == "__main__":
    main()
