import os

filepath = os.path.join(os.path.dirname(__file__), "rosalind_dna.txt")

with open(filepath) as f:
    dna_string = f.read()

counts = {"A": 0, "C": 0, "G": 0, "T": 0}

for i in range(len(dna_string)):
    counts[dna_string[i]] += 1

print(counts["A"], counts["C"], counts["G"], counts["T"])