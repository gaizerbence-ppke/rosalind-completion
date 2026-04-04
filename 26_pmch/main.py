import os
import benczutils.bio as bio
import math

def countMatchings(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        fasta = bio.readFasta(f.read())

        for gene in fasta:
            sequence = fasta[gene]
            A = 0
            G = 0
            for i in range(len(sequence)):
                if sequence[i] == 'A':
                    A += 1
                if sequence[i] == 'G':
                    G += 1
            #print(f"In {sequence}: {A} A and {G} G")
            return math.factorial(A) * math.factorial(G)
        
print(countMatchings("sample.txt"))
print(countMatchings("rosalind_pmch.txt"))