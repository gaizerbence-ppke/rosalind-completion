import os
import numpy as np

def calculateProbability(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        raw = f.readline().strip().split(' ')
        k = int(raw[0])
        N = int(raw[1])
    pascalrow = np.array([1])
    for _ in range(pow(2,k)):
        pascalrow = np.concatenate((np.zeros(1), pascalrow/4)) + np.concatenate((pascalrow *3 / 4, np.zeros(1)))
    print(sum(pascalrow[N:]))
    
    

calculateProbability("sample.txt")
calculateProbability("rosalind_lia.txt")