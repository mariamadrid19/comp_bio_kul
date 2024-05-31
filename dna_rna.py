# DNA coding strand (this is the DNA sequence we want to convert to a protein)
DNA_seq = "ATGTTCCATCGCTATGAAGCCTAA"

def transcribe(seq):
    RNA = seq.replace("T", "U")
    return str(RNA)

def translate(seq) :
    mRNA_AA_table = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
            "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
            "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
            "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr", "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
            "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop", "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
            "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
            "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
            "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"}
    protein = ""
    for i in range(0, len(seq), 3) :
        codon = seq[i:i+3]
        protein = protein + mRNA_AA_table[codon]
    return str(protein)

import translation
import transcription 

mRNA = transcription.transcribe(DNA_seq)
print("mRNA: ", mRNA)
type(mRNA)

protein = translation.translate(mRNA)
print("Protein: ", protein)
type(protein)
