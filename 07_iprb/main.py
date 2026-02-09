import os

def get_dominant_phenotype_probability(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as f:
        counts_string = f.readline().strip().split(' ')
        counts = [int(x) for x in counts_string]
    N = sum(counts)
    k = counts[0]
    m = counts[1]
    n = counts[2]

    twoDom = k * (k - 1) / N / (N - 1)
    twoHetero = m * (m - 1) / N / (N - 1)
    twoRec = n * (n - 1) / N / (N - 1)
    DomHet = k * m / N / (N - 1) * 2
    DomRec = k * n / N / (N - 1) * 2
    HetRec = m * n / N / (N - 1) * 2

    return (twoDom + DomHet + DomRec + twoHetero * 3 / 4 + HetRec / 2)

print(get_dominant_phenotype_probability("sample.txt"))
print(get_dominant_phenotype_probability("rosalind_iprb.txt"))