
import os

def solveProblem(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        numNodes = int(f.readline().strip())
        numLines = f.read().strip().count('\n')
        print(f"{numNodes} nodes, {numLines + 1} vertices")
        return numNodes - numLines - 2

print(solveProblem("sample.txt"))
print("########################")
print(solveProblem("rosalind_tree.txt"))
            