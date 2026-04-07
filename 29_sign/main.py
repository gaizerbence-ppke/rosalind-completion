import os
import math
import benczutils.common as common

def listSignedPermutations(filename):
    length = 0
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        length = int(f.readline().strip())
    permutations = [list(map(lambda x : x + 1, p)) for p in common.getPermutations(length)]
    signedPermutations = []
    for perm in permutations:
        signs = [0] * length
        for i in range(1 << length):
            signedPermutations.append([(element if signs[idx] == 0 else -element) for idx, element in enumerate(perm)])
            signs[-1] += 1
            for i in reversed(range(length)):
                if i > 0 and signs[i] > 1:
                    signs[i] = 0
                    signs[i - 1] += 1
    return signedPermutations

signed = listSignedPermutations("sample.txt")
for perm in signed:
    print(" ".join(map(str, perm)))

signed = listSignedPermutations("rosalind_sign.txt")
with open("out.txt", mode="w") as f:
    f.write(str(len(signed)))
    f.write('\n')
    for perm in signed:
        f.write(" ".join(map(str, perm)))
        f.write('\n')