# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence

    """
    transcribed_seq = ""
    for nucleotide in seq:
        #extracts the value from the dictionary, so the RNA nucleotide
        if nucleotide == "T":
            transcribed_seq += "U"
        else:
            transcribed_seq += str(nucleotide)
    
    print(transcribed_seq)

    pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence. 
    -> so converting RNA back into DNA
    """
    rev_transcribed_seq = ""
    for nucleotide in seq:
        if nucleotide == "U":
            rev_transcribed_seq += "T"
        else: 
            rev_transcribed_seq += nucleotide

    print(rev_transcribed_seq)

    pass

#testing 
transcribe("ATGCCT")
reverse_transcribe("UACGGA")
