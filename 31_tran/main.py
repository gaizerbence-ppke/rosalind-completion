
import os
import benczutils.bio as bio

categories = {'A': 0, 'T': 1, 'G': 0, 'C': 1}

def solveProblem(filename):
    transitions = 0
    transversions = 0
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        fasta = bio.readFasta(f.read())
        s1 = fasta[list(fasta.keys())[0]]
        s2 = fasta[list(fasta.keys())[1]]
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]: continue
        if categories[s1[i]] == categories[s2[i]]: transitions += 1
        else: transversions += 1

    return transitions / transversions

print(solveProblem("sample.txt"))
print("########################")
print(solveProblem("rosalind_tran.txt"))
            