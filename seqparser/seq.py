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
        transcribed_seq += TRANSCRIPTION_MAPPING[nucleotide]
    return transcribed_seq
    

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

    return rev_transcribed_seq

    pass

#testing 
print(transcribe("ATGCCT"))      
print(reverse_transcribe("UACGGA"))
