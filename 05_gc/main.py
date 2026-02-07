import os

def calculateGC(dna_string):
    GC = sum((1 if nucl in "GC" else 0 for nucl in dna_string))
    return round(GC / len(dna_string) * 100, 5)

def find_best_GC(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    FASTA = {}
    with open(filepath) as f:
        while True:
            currentLine = f.readline()
            if len(currentLine) <= 0:
                break
            if currentLine[0] == '>':
                currentKey = currentLine[1:].strip()
                FASTA[currentKey] = ""
            else:
                FASTA[currentKey] += currentLine.strip()
                
    bestVal = -1
    bestKey = None
    for key in FASTA:
        val = calculateGC(FASTA[key])
        if val > bestVal:
            bestVal = val
            bestKey = key
    return (bestKey, bestVal)
    
print(find_best_GC("sample.txt"))
res = (find_best_GC("rosalind_gc.txt"))
print(res[0])
print(res[1])