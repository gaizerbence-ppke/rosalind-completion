import os

def read_codon_table(filename):
    codon_table = {}
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        for line in f:
            linearrs = line.strip().split()
            for pair in zip(linearrs[0::2], linearrs[1::2]):
                codon_table[pair[0]] = pair[1]
    return codon_table

def translate_RNA(filename, codon_table):
    protein = ""
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        rna = f.read().strip()
        cursor = 0
        while cursor < len(rna):
            next_codon = rna[cursor:(cursor + 3)]
            amino_acid = codon_table[next_codon]
            if amino_acid == "Stop":
                break
            protein += amino_acid
            cursor += 3
    return protein

codons = read_codon_table("codon_table.txt")
print(translate_RNA('sample.txt', codons))
print(translate_RNA('rosalind_prot.txt', codons))