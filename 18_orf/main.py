import os
from benczutils import bio

def findFrames(rna):
    frames = set()
    cursor = 0
    while cursor + 2 < len(rna):
        codon = ''.join(rna[cursor:cursor + 3])
        if codon == 'AUG':
            protein = ""
            nestedCursor = cursor
            while nestedCursor + 2 < len(rna):
                codon = rna[nestedCursor:(nestedCursor + 3)]
                aa = bio.CODON_TABLE[codon]
                if aa == 'X':
                    frames.add(protein)
                    break
                else:
                    protein += aa
                nestedCursor += 3
        cursor += 3
    return frames
def findOpenFrames(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        genes = bio.readFasta(f.read())
    for key in genes:
        gene = genes[key]
        frames = set()
        forward_rna = "".join(bio.complement_Dna2Rna(gene))
        backward_rna = "".join(bio.complement_Rna2Rna(forward_rna))
        for phase in [0, 1, 2]:
            frames = frames.union(findFrames(forward_rna[phase:]))
            frames = frames.union(findFrames(backward_rna[phase:]))
        for frame in frames:
            print(frame)


findOpenFrames("sample.txt")
print("==================================")
findOpenFrames("rosalind_orf.txt")