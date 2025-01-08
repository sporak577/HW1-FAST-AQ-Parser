# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()

#reversing key:value pair from TRANSCRIPTION_MAPPING
REVERSE_MAPPING = {v : k for k, v in TRANSCRIPTION_MAPPING.items()}

def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence

    comments:
    I had to use chatgpt to explain to me how the code is set up e.g. I didn't know what from typing import Union means. 
    Further, I had to use chatgpt to tell me how to retreive the value from the key in a dictionary, as I had forgotten it.
    """
    transcribed_seq = ""
    for nucleotide in seq:
        #extracts the value from the dictionary, so the RNA nucleotide
        transcribed_seq += TRANSCRIPTION_MAPPING[nucleotide]
    print(transcribed_seq)

   

    pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence. 
    -> so converting RNA back into DNA?
    """
    rev_transcribed_seq = ""
    for nucleotide in seq:
        rev_transcribed_seq += REVERSE_MAPPING[nucleotide]
    print(rev_transcribed_seq)

    pass

#testing 
transcribe("ATGCCT")
reverse_transcribe("UACGGA")
