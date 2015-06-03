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

    def test_get_genes_from_file(self):
        expected = 95
        result = alignme.get_genes_from_file(self.fasta_file)
        self.assertEqual(expected, result)
