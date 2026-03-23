import os
import benczutils.bio as bio

def findPalindromes(filename):
    palindromes = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        fasta = bio.readFasta(f.read())
        for key in fasta:
            seq = fasta[key]

            minLength = 4
            maxLength = 12
            for start in range(len(seq)):
                for length in range(minLength, maxLength + 1):
                    end = start + length
                    if end >= len(seq) + 1:
                        continue
                    DNAstring = seq[start:end]
                    reverse = bio.complement_Dna2Dna(DNAstring)
                    if DNAstring == "".join(reverse):
                        palindromes.append((start, length))
    return palindromes
                    

pal = findPalindromes("sample.txt")
for p in pal:
    print(p[0] + 1, p[1])

pal = findPalindromes("rosalind_revp.txt")
for p in pal:
    print(p[0] + 1, p[1])