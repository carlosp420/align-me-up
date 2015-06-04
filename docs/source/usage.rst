Usage
=====

Run from the command line:

.. code-block:: shell

    python alignme.py -i input_file.fasta


API
---

How to get consensus sequences:

    >>> from utils import Assembler
    >>> list_of_seq_records = []
    >>> assembler = Assembler(list_of_seq_records)
    >>> # returns consensus sequence
