from benczutils import bio
import os

def potentialmrnas(filename):
    paths = {}
    for key in bio.CODON_TABLE:
        if bio.CODON_TABLE[key] in paths:
            paths[bio.CODON_TABLE[key]] += 1
        else:
            paths[bio.CODON_TABLE[key]] = 1
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        protein = f.readline().strip()
        protein += "X"

        ways = 1
        for aa in protein:
            ways *= paths[aa]
            ways %= 1_000_000
        print(ways)

potentialmrnas("sample.txt")
potentialmrnas("rosalind_mrna.txt")