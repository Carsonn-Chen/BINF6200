from Bio import SeqIO
from Bio.Seq import Seq

with open("rosalind_splc.txt") as f:
    Seqs = list(SeqIO.parse(f, "fasta"))
    Seqs = [str(fasta.seq) for fasta in Seqs]
    # print(Seqs)

for i in range(1, len(Seqs)):
    Seqs[0] = Seqs[0].replace(Seqs[i], '')
    # print(Seqs[0])

Seqs[0] = Seq(Seqs[0])
print(Seqs[0].translate(to_stop=True))
