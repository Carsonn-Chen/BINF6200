from Bio import SeqIO

with open("rosalind_lcsm.txt", "r") as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))
    sequences = [str(fasta.seq) for fasta in fasta_sequences]


def is_substr(sub_str, seqs):
    if len(seqs) < 1 and len(sub_str) < 1:
        return False
    for seq in seqs:
        if sub_str not in seq:
            return False
    return True


substr = ''
for i in range(len(sequences[0])):
    for j in range(len(sequences[0]) - i + 1):
        if j > len(substr) and is_substr(sequences[0][i: i + j], sequences):
            substr = sequences[0][i: i + j]

print(substr)