import os

def createAdjecencyList(filename):
    genes = {}
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        current = ""
        while True:
            line = f.readline().strip()
            if len(line) <= 0:
                break
            if line.startswith('>'):
                current = line[1:]
                genes[current] = ""
            else:
                genes[current] += line
    adj_list = []
    for firstKey in genes.keys():
        for secondKey in genes.keys():
            if firstKey == secondKey:
                continue
            if genes[firstKey][-3:] == genes[secondKey][:3]:
                adj_list.append(f"{firstKey} {secondKey}")
    print("\n".join(adj_list))

createAdjecencyList("sample.txt")
print()
createAdjecencyList("rosalind_grph.txt")