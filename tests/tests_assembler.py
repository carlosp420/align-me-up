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

    def test_guess_best_kmer(self):
        velvet_params = {
            1: {'max': '1', 'n50': '1', 'nodes': '4', 'total': '4'},
            3: {'max': '1', 'n50': '1', 'nodes': '40', 'total': '40'},
            5: {'max': '1', 'n50': '1', 'nodes': '435', 'total': '426'},
            7: {'max': '4', 'n50': '1', 'nodes': '7248', 'total': '7136'},
            9: {'max': '20', 'n50': '3', 'nodes': '16387', 'total': '32363'},
            11: {'max': '77', 'n50': '8', 'nodes': '8682', 'total': '36061'},
            13: {'max': '124', 'n50': '21', 'nodes': '5807', 'total': '45603'},
            15: {'max': '168', 'n50': '33', 'nodes': '3920', 'total': '58584'},
            17: {'max': '212', 'n50': '41', 'nodes': '3927', 'total': '62871'},
            19: {'max': '370', 'n50': '67', 'nodes': '2782', 'total': '69153'},
            21: {'max': '795', 'n50': '104', 'nodes': '1807', 'total': '70823'},
            23: {'max': '797', 'n50': '122', 'nodes': '1718', 'total': '70649'},
            25: {'max': '1097', 'n50': '181', 'nodes': '1044', 'total': '67531'},
            27: {'max': '1318', 'n50': '264', 'nodes': '615', 'total': '61967'},
            29: {'max': '1530', 'n50': '300', 'nodes': '591', 'total': '60406'},
            31: {'max': '1665', 'n50': '381', 'nodes': '410', 'total': '56036'},
        }
        expected = 31
        result = self.assembler.guess_best_kmer(velvet_params)
        self.assertEqual(expected, result)

    def test_velvet_step2(self):
        best_input_kmer = 31
        result = self.assembler.velvet_step2(best_input_kmer)
        self.assertEqual(0, result)

    def tearDown(self):
        try:
            os.remove('assembly_velvet.sh')
        except FileNotFoundError:
            pass

        try:
            os.remove('assembly_velvet2.sh')
        except FileNotFoundError:
            pass
