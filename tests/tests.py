# -*- coding: utf-8 -*-
import os
import sys
import unittest

from Bio import SeqIO

from alignme import alignme


class TestAlignme(unittest.TestCase):
    def setUp(self):
        self.fasta_file = 'tests/test.fasta'

    def test_read_fasta(self):
        for seq_record in SeqIO.parse(self.fasta_file, 'fasta'):
            seq = seq_record.seq
            break
        self.assertEqual(105, len(seq))

    def test_get_gene_from_fasta_id(self):
        my_string = 'BGIBMGA010002-TA-NW_G001_gi|440271108|gb|AHIO01003419.1|:1071-1175 NW_G001 sequence homologous to BGIBMGA010002-TA:557-591'
        expected = 'BGIBMGA010002'
        result = alignme.get_gene_from_fasta_id(my_string)
        self.assertEqual(expected, result)


