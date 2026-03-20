import os

from benczutils import bio

def findMotif(filename):
    accessIDs = []
    glycosilation_motif = bio.Motif("N{P}[ST]{P}")
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        for line in f:
            full_id = line.strip()
            id = full_id.split('_')[0]
            if len(id) == 0:
                continue
            accessIDs.append(line.strip())
            genes = bio.getFasta(id)
            for key in genes:
                gene = genes[key]
                locations = []
                for i in range(len(gene) - glycosilation_motif.motif_length):
                    if glycosilation_motif.check(gene[i:(i+glycosilation_motif.motif_length)]):
                        locations.append(i + 1)
                if len(locations) > 0:
                    print(full_id)
                    print(" ".join(map(str, locations)))

findMotif("sample.txt")
print("--------------------------")
findMotif("rosalind_mprt.txt")