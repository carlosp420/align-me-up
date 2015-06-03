# -*- coding: utf-8 -*-

__author__ = 'carlosp420'

import argparse

from Bio import SeqIO


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
    split_file_by_gene(args)


def split_file_by_gene(args):
    filename = args.fasta_file
    genes = get_genes_from_file(filename)


def get_genes_from_file(filename):
    genes = set()
    for seq_record in SeqIO.parse(filename, 'fasta'):
        id = seq_record.id
        id = id.split('-')
        gen = id[0]
        genes.add(gen)
    return genes


def main():
    parser = create_parser()
    args = parser.parse_args()
    get_started(args)


if __name__ == "__main__":
    main()
