# -*- coding: utf-8 -*-

__author__ = 'carlosp420'

import argparse
import os

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
    # for each file
    #     split by specimen in batches
    #     for each batch
    #         if sequence is genomic,
    #     for each bach
    #         do consensus, assembly
    #     align sequences in file


def split_file_by_gene(args):
    filename = args.fasta_file
    for seq_record in SeqIO.parse(filename, 'fasta'):
        gene = get_gene_from_fasta_id(seq_record.id)
        target_filename = make_filename_for_gene(gene)
        if gene in seq_record.id:
            with open(target_filename, 'a') as handle:
                handle.write('>' + seq_record.id + '\n' + str(seq_record.seq) + '\n')


def get_gene_from_fasta_id(id):
    id = id.split('-')
    gene = id[0]
    return gene


def make_filename_for_gene(gene):
    target_filename = "gene_{}.fasta".format(gene)
    if not os.path.isfile(target_filename):
        with open(target_filename, 'w') as handle:
            handle.write('')
    return target_filename


def main():
    parser = create_parser()
    args = parser.parse_args()
    get_started(args)


if __name__ == "__main__":
    main()
