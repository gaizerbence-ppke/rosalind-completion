import os

def transcribe_RNA(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as f:
        rna_string = f.read().strip()
    rna_modified = "".join((("U" if nucl == "T" else nucl) for nucl in rna_string))
    print(rna_modified)

transcribe_RNA("sample.txt")
transcribe_RNA("rosalind_rna.txt")