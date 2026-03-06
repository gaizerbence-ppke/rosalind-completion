import os

def findCommonSegment(filename):
    genes = {}
    reference = ""
    referenceLength = 9999999
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
                if len(current) > 0 and len(genes[current]) < referenceLength:
                    referenceLength = len(genes[current])
                    reference = current
                genes[current] += line
    start = 0
    end = 0
    longestSegment = ""
    while end < len(genes[reference]):
        segment = genes[reference][start:end]
        good = True
        for key in genes:
            if key == reference:
                continue
            if segment not in genes[key]:
                start += 1
                good = False
                break
        if good:
            if len(segment) > len(longestSegment):
                longestSegment = segment
            end += 1
    print(longestSegment)

findCommonSegment("sample.txt")
findCommonSegment("rosalind_lcsm.txt")