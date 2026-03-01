import os

def expectedNumberOfDominantFenotype(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        inputs = f.readline().strip().split(' ')

    AAAA = int(inputs[0])
    AAAa = int(inputs[1])
    AAaa = int(inputs[2])
    AaAa = int(inputs[3])
    Aaaa = int(inputs[4])
    aaaa = int(inputs[5])

    expected = 0

    expected += AAAA * 1
    expected += AAAa * 1
    expected += AAaa * 1
    expected += AaAa * 0.75
    expected += Aaaa * 0.5
    expected += aaaa * 0

    return expected * 2

print(expectedNumberOfDominantFenotype("sample.txt"))
print(expectedNumberOfDominantFenotype("rosalind_iev.txt"))