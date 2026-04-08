import os
import benczutils.bio as bio

def findSplicedMotif(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        fasta = bio.readFasta(f.read().strip())
    seq = fasta[list(fasta.keys())[0]]
    subseq = fasta[list(fasta.keys())[1]]
    motifIdx = 0
    locations = []
    for idx in range(len(seq)):
        char = seq[idx]
        if char == subseq[motifIdx]:
            locations.append(idx + 1)
            motifIdx += 1
            if motifIdx >= len(subseq):
                break
    return locations

print(" ".join(map(str, findSplicedMotif("sample.txt"))))
print(" ".join(map(str, findSplicedMotif("rosalind_sseq.txt"))))