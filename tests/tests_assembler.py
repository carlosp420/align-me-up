# -*- coding: utf-8 -*-
import os
import unittest

from Bio import SeqIO

from alignme.utils import Assembler
from alignme import BASEDIR


class TestAssembler(unittest.TestCase):
    def setUp(self):
        lista = []
        for seq_record in SeqIO.parse('tests/test_gene_BGIBMGA010002.fasta', 'fasta'):
            lista.append(seq_record)

        self.assembler = Assembler(lista)

    def test_downloading_velvet_scripts(self):
        self.assembler.get_velvet_scripts()

        with open(os.path.join(BASEDIR, 'alignme', 'assembly_velvet.sh'), 'r') as handle:
            script_content = handle.read()

        self.assertTrue('fastq' not in script_content)

    def test_velvet_step1(self):
        result = self.assembler.velvet_step1()
        self.assertIsNotNone(result)

    def test_get_velvet_params(self):
        output = self.assembler.velvet_step1()
        result = self.assembler.get_velvet_params(output)
        self.assertTrue(29 in result)

    def tearDown(self):
        try:
            os.remove('assembly_velvet.sh')
        except FileNotFoundError:
            pass

        try:
            os.remove('assembly_velvet2.sh')
        except FileNotFoundError:
            pass
