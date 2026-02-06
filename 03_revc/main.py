import os

def complement_nucleotid(nucl):
    if nucl == "A":
        return "T"
    if nucl == "T":
        return "A"
    if nucl == "G":
        return "C"
    if nucl == "C":
        return "G"
def complement_DNA(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as f:
        dna_string = f.read().strip()
    complement = "".join((complement_nucleotid(nucl) for nucl in dna_string))
    print(complement[::-1])

complement_DNA("sample.txt")
complement_DNA("rosalind_revc.txt")