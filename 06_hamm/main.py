import os

def count_point_mutations(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as f:
        original = f.readline().strip()
        mutated = f.readline().strip()
    return sum((0 if orig == mut else 1 for orig, mut in zip(original, mutated)))

print(count_point_mutations("sample.txt"))
print(count_point_mutations("rosalind_hamm.txt"))