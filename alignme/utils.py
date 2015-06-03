# -*- coding: utf-8 -*-

__author__ = 'carlosp420'

import re


class IntronWasher(object):
    """Input a FASTA sequence object and returns it after removing any intron if necessary.
    """
    def __init__(self, seq_record):
        self.sequence = seq_record.seq
        self.sequence_string = str(seq_record.seq)

    def identify_orf(self):
        """Idenfify open reading frame.
        Taken from http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16
        """
        print("Trying to identify ORF")
        stop_codons = [
            'TAA', 'TGA', 'TAG',
            'TTA', 'TCA', 'CTA',
        ]
        combined = '(' + ')|('.join(stop_codons) + ')'
        if re.search(combined, self.sequence_string):
            print('math')
