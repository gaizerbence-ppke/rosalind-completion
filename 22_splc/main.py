import os
import benczutils.bio as bio

def getExtrons(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        fasta = bio.readFasta(f.read())
        
        gene = ""
        introns = []

        first = True
        for key in fasta:
            if first:
                first = False
                gene = fasta[key]
            else:
                introns.append(fasta[key])
        extrons = ""
        cursor = 0
        while cursor < len(gene):
            for intron in introns:
                if intron == gene[cursor:cursor+len(intron)]:
                    cursor += len(intron)
                    break
            extrons += gene[cursor]
            cursor += 1
        rna = bio.complement_Rna2Rna(bio.complement_Dna2Rna(extrons))
        protein = ""
        for aaId in range(len(extrons) // 3):
            aa = bio.CODON_TABLE["".join(rna[3 * aaId:(3 * aaId + 3)])]
            if aa == 'X':
                break
            protein += aa
        return protein

print(getExtrons("sample.txt"))
print(getExtrons("rosalind_splc.txt"))