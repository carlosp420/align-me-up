# -*- coding: utf-8 -*-

__author__ = 'carlosp420'

import os
import re
import subprocess
import uuid

import requests
from Bio import SeqIO

from alignme import BASEDIR


class IntronWasher(object):
    """Input a FASTA sequence object and returns it after removing any intron if necessary.
    """
    def __init__(self, seq_record):
        self.sequence = seq_record.seq
        self.sequence_string = str(seq_record.seq)

    def identify_orf(self):
        """Idenfify open reading frame.
        Taken from http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16
        """
        print("Trying to identify ORF")
        stop_codons = [
            'TAA', 'TGA', 'TAG',
            'TTA', 'TCA', 'CTA',
        ]
        combined = '(' + ')|('.join(stop_codons) + ')'
        if re.search(combined, self.sequence_string):
            print('math')


class Assembler(object):
    """Takes a list of sequence objects that belong to the same gene and specimen, assemble
    and return consensus sequence.
    """
    def __init__(self, list_of_seq_records):
        self.list_of_seq_records = list_of_seq_records
        self.filename = self._write_to_file()

    def _write_to_file(self):
        filename = '{}.fasta'.format(os.path.join(BASEDIR, str(uuid.uuid4())))
        SeqIO.write(self.list_of_seq_records, filename, "fasta")
        return filename

    def run_velvet(self):
        """
        Do *de novo* assembly of expected sequences of a FASTA nucleotide file.
        """
        self.get_velvet_scripts()

        output = self.velvet_step1()
        velvet_params = self.get_velvet_params(output)
        best_input_kmer = self.guess_best_kmer(velvet_params)

        assembly = self.velvet_step2(best_input_kmer)

        if assembly == 0:
            if self.count_reads("test/contigs.fa", "fasta") > 0:
                print("The assembly produced " + str(self.count_reads("test/contigs.fa", "fasta")) + " potential contigs")
                filename = re.sub(".fastq$", "", fastq_file) + "_assembled.fasta"
                os.rename("test/contigs.fa", filename)
                print("Assembled sequence has been saved as file " + filename)

    def get_velvet_scripts(self):
        if not os.path.isfile(os.path.join(BASEDIR, 'alignme', 'assembly_velvet.sh')):
            # downloading scripts to local folder
            r = requests.get("https://raw.github.com/carlosp420/PyPhyloGenomics/master/assembly_velvet.sh")
            f = open(os.path.join(BASEDIR, 'alignme', 'assembly_velvet.sh'), 'w')
            f.write(r.content.decode('utf-8').replace("fastq", "fasta"))
            f.close()

            r = requests.get("https://raw.github.com/carlosp420/PyPhyloGenomics/master/assembly_velvet2.sh")
            f = open(os.path.join(BASEDIR, 'alignme', 'assembly_velvet2.sh'), 'w')
            f.write(r.content.decode('utf-8').replace("fastq", "fasta"))
            f.close()

    def velvet_step1(self):
        command = "bash {} {}".format(
            os.path.join(BASEDIR, 'alignme', 'assembly_velvet.sh'),
            os.path.join(BASEDIR, self.filename)
        )
        output = subprocess.check_output(command, shell=True)
        return output

    def get_velvet_params(self, input):
        """
        :param input: data from runing velvet assembly on all Kmer values
        :return: a dictionary with the parameters: kmer, nodes, n50, max, total
        """
        lines = input.decode('utf-8')
        lines = lines.split("\n")
        mydict = dict()
        kmer = 31
        for line in lines:
            if "n50" in line:
                lista = dict()
                nodes = re.search("(\d+)\snodes", line)
                nodes = nodes.groups()[0]
                lista['nodes'] = nodes

                n50 = re.search("n50 of (\d+)", line)
                n50 = n50.groups()[0]
                lista['n50'] = n50

                maxim = re.search("max\s(\d+)", line)
                maxim = maxim.groups()[0]
                lista['max'] = maxim

                total = re.search("total\s(\d+)", line)
                total = total.groups()[0]
                lista['total'] = total

                mydict[kmer] = lista
                kmer -= 2
        return mydict

    def guess_best_kmer(self, velvet_params):
        """
        :param velvet_params: params from two runs of velvet on all Kmer values these inputs are dictionaries.
        :return: a list containing:
                 - the filtered file number either filter2 or filter3
                 - the best kmer value found by comparison of the two
        """
        n50 = []
        for i in velvet_params:
            n50.append(int(velvet_params[i]['n50']))
            n50.sort()
            n50.reverse()
        filtered = n50[0]

        for i in velvet_params:
            if velvet_params[i]['n50'] == str(filtered):
                return(i)

    def velvet_step2(self, best_input_kmer):
        command = "bash {} test {} .fasta {}".format(
            os.path.join(BASEDIR, 'alignme', 'assembly_velvet2.sh'),
            os.path.join(BASEDIR, self.filename),
            str(best_input_kmer),
        )
        assembly = subprocess.check_call(command, shell=True)
        return assembly

    def count_reads(self, fastqFile, file_format):
        """
        Internal function
        """
        count = 0
        for seq_record in SeqIO.parse(fastqFile, file_format):
            count = count + 1
        return(count)

    def get_statistics_using_oases(self):
        pass
