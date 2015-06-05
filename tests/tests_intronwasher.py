# -*- coding: utf-8 -*-
import os
import sys
import unittest

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from alignme.utils import IntronWasher


class TestIntronWasher(unittest.TestCase):
    def setUp(self):
        simple_seq = Seq('AATTTTCAGGTGGCACTTGAAGAATTAGGTGCAGACTTCAATCAAGACTGGAAAGGTTTCCAGCAGGCCTGCATCAAAGCTTTATTGAAAGAAGCCAAAGAAAAG')
        self.seq_record = SeqRecord(simple_seq)

    def test_getting_seq_as_string(self):
        expected = 'AATTTTCAGGTGGCACTTGAAGAATTAGGTGCAGACTTCAATCAAGACTGGAAAGGTTTCCAGCAGGCCTGCATCAAAGCTTTATTGAAAGAAGCCAAAGAAAAG'
        washer = IntronWasher(self.seq_record)
        result = washer.sequence_string
        self.assertEqual(expected, result)
