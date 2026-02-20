import os

def find_consensus(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        first = True
        counts = []
        writecursor = 0
        for line in f:
            if line.startswith('>'):
                writecursor = 0
                continue
            gene = line.strip()
            for readcursor in range(len(gene)):
                if len(counts) < writecursor + 1:
                    counts.append({'A': 0, 'T': 0, 'C': 0, 'G': 0})
                counts[writecursor][gene[readcursor]] += 1
                writecursor += 1
    
    consensus = ''
    for count in counts:
        consensus += max(count, key=count.get)
    print(consensus)
    for key in 'ATCG':
        print(f"{key}: {' '.join(str(count[key]) for count in counts)}")

print(find_consensus('sample.txt'))
print(find_consensus('rosalind_cons.txt'))