import os

def getLongestIncreasing(sequence):
    besties = [[]]
    for number in sequence:
        for length in reversed(range(len(besties))):
            if length == 0 or number > besties[length][-1]:
                if len(besties) <= length + 1:
                    besties.append(besties[length] + [number])
                elif besties[length + 1][-1] > number:
                    besties[length + 1] = besties[length] + [number]
    return besties[-1]

def getBothSubsequences(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        f.readline()
        sequence = list(map(int, f.readline().strip().split(' ')))
        print(" ".join(map(str, getLongestIncreasing(sequence))))
        print(" ".join(map(str, list(reversed(getLongestIncreasing(reversed(sequence)))))))
        

        
getBothSubsequences("sample.txt")
getBothSubsequences("rosalind_lgis.txt")