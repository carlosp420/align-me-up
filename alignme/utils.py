# -*- coding: utf-8 -*-

__author__ = 'carlosp420'


class IntronWasher(object):
    """Input a FASTA sequence object and returns it after removing any intron if necessary.
    """
    def __init__(self, seq_record):
        self.mystring = seq_record
        #self.sequence_string = str(seq_record.seq)
        #self.sequence = seq_record.seq
