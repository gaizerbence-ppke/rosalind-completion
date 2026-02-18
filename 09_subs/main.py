import os

def find_occurances(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        dna = f.readline().strip()
        pattern = f.readline().strip()
        occurances = []

        for start in range(len(dna) - len(pattern) + 1):
            if dna[start:(start + len(pattern))] == pattern:
                occurances.append(start + 1)
        return occurances
    
print(find_occurances('sample.txt'))
print(" ".join(map(str, find_occurances('rosalind_subs.txt'))))