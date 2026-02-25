import os

def fibd(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        inputData = f.readline().strip().split(' ')
        n = int(inputData[0])
        m = int(inputData[1])
    ageDistribution = [0] * m
    ageDistribution[-1] = 1

    for step in range(n - 1):
        ageDistribution.append(sum(ageDistribution[:-1]))
        ageDistribution.pop(0)
        #print(ageDistribution)
    print(sum(ageDistribution))

fibd("sample.txt")
fibd("rosalind_fibd.txt")