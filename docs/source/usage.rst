Usage
=====

Run from the command line:

.. code-block:: shell

    python alignme.py -i input_file.fasta


API
---

How to remove intron from a sequence:

.. doctest::

    >>> from alignme.utils import IntronWasher
    >>> washer = IntronWasher()
    >>> washer.clean
    'hola'
