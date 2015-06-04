# -*- coding: utf-8 -*-
import os
import unittest


from alignme.utils import Assembler


class TestAssembler(unittest.TestCase):
    def setUp(self):
        self.assembler = Assembler([])

    def test_downloading_velvet_scripts(self):
        self.assembler.get_velvet_scripts()

        with open('assembly_velvet.sh', 'r') as handle:
            script_content = handle.read()

        self.assertTrue('fastq' not in script_content)

    def tearDown(self):
        try:
            os.remove('assembly_velvet.sh')
        except FileNotFoundError:
            pass

        try:
            os.remove('assembly_velvet2.sh')
        except FileNotFoundError:
            pass
