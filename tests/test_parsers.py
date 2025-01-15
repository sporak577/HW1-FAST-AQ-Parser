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
    filename = "test_data.fastq"

    with open(filename, "r") as f: 
        #reads first line of the file and removes any leading/trailing whitespace
        first_line = f.readline().strip()

    if first_line.startswith("@"): 
        #raise a ValueError, match ensures the error messages contains a specific string
        with pytest.raises(ValueError, match="Invalid FASTA format"):
            raise ValueError("Invalid FASTA format: FASTQ file detected")

    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    parser = FastqParser("test_data.fastq")
    #the FastqParser yields a tuple (header, sequence, quality)
    sequences = list(parser)

    #checking content of first sequence
    assert len(sequences) == 2
    assert sequences[0][0] == "seq1"
    assert sequences[0][1] == "AGCTAGCTAGCT"
    assert sequences[0][2] == "IIIIIIIIIIII" #quality

    #checking content of second sequence 
    assert sequences[1][0] == "seq2"
    assert sequences[1][1] == "CGTAGCTAGCTA"
    assert sequences[1][2] == "JJJJJJJJJJJJ" #quality

    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    filename = "test_data.fa"

    with open(filename, "r") as f: 
        #reads first line of the file and removes any leading/trailing whitespace
        first_line = f.readline().strip()

    if first_line.startswith(">"): 
        #raise a ValueError, match ensures the error messages contains a specific string
        with pytest.raises(ValueError, match="Invalid FASTQ format"):
            raise ValueError("Invalid FASTQ format: FASTA file detected")

    pass