# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    #creating an instance of FastaParser and passing the test file path
    #this is the first time I am doing this so I am getting help from AI!
    parser = FastaParser("test_data.fa")
    #using list() to consume the iterable and get all sequences
    #collects records into a list, where each record is a tuple representing a sequence
    #e.g. sequences = [("seq1, 'sequence"), ("seq2", "sequence2" )]
    sequences = list(parser)
    #this checks that the number of sequences of my file is 2
    assert len(sequences) == 2
    #check the content of first sequences
    assert sequences[0][0] == "seq1"
    assert sequences[0][1] == "GGCTAGCTAGTC"

    assert sequences[1][0] == "seq2"
    assert sequences[1][1] == "CGTATACTAGCA"


    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    parser = FastaParser("test_data.fastq")
    #expected to raise a ValueError for invalid format
    with pytest.raises(ValueError):  
        #list(parser) should raise an error as the parser encounters lines it cannot interprest as FASTA
        sequences = list(parser) 
    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    pass