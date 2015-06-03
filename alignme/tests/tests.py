# -*- coding: utf-8 -*-
import unittest

from Bio import SeqIO


class TestAlignme(unittest.TestCase):
    def test_read_fasta(self):
        for seq_record in SeqIO.parse('alignme/tests/test.fasta', 'fasta'):
            seq = seq_record.seq
            break
        self.assertEqual(105, len(seq))
