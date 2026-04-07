import os
import math

def calculateRandomStringProbabilities(filename):
    probabilities = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        bases = list(f.readline().strip())
        print(bases)
        gc_ratios = list(map(float, f.readline().strip().split(' ')))
        print(gc_ratios)
        for ratio in gc_ratios:
            gc_prob = math.log10(ratio / 2)
            at_prob = math.log10((1 - ratio) / 2)
            probability = 0
            for base in bases:
                if base in "AT":
                    probability += at_prob
                if base in "GC":
                    probability += gc_prob
            probabilities.append(probability)
    return probabilities

probabilities = calculateRandomStringProbabilities("sample.txt")
print(" ".join([str(round(a, 3)) for a in probabilities]))

probabilities = calculateRandomStringProbabilities("rosalind_prob.txt")
print(" ".join([str(round(a, 3)) for a in probabilities]))