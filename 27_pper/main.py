import os

def countPartialPermutations(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        line = f.readline().strip()
        n, k = map(int, line.split())
        result = 1
        for i in range(n, n-k, -1):
            result *= i
            result = result % 1000000
        return result
    
print(countPartialPermutations("sample.txt"))
print(countPartialPermutations("rosalind_pper.txt"))