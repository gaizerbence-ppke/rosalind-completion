import os
import benczutils.common as common

def getPermutations(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        length = int(f.readline().strip())
    return common.getPermutations(length)

perm1 = getPermutations("sample.txt")

print(len(perm1))
for line in perm1:
    print(' '.join(map(str, map(lambda a : a + 1, line))))

perm2 = getPermutations("rosalind_perm.txt")
print(len(perm2))
for line in perm2:
    print(' '.join(map(str, map(lambda a : a + 1, line))))