from Bio import SeqIO

with open("rosalind_revp.txt") as f:
    Seq = SeqIO.read(f, format="fasta")
    Seq = Seq.seq

for i in range(len(Seq)):
    for j in range(i+3, len(Seq)):
        if j - i >= 12:
            break
        # print(i, Seq[i:j+1], Seq[i:j+1].reverse_complement())
        if Seq[i:j+1] == Seq[i:j+1].reverse_complement():
            print(i+1, j-i+1)