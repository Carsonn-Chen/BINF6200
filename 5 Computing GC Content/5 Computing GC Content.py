fasta_seq = {}

with open("rosalind_gc.txt") as f:
    seq = ""
    name = ""
    for line in f:
        if line.startswith(">"):
            if len(seq) > 1:
                fasta_seq[name] = seq
                seq = ""
            name = line[1:].strip()
        else:
            seq += line.strip()
    fasta_seq[name] = seq


# print(fasta_seq)

def calc_cg(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)


max_key, max_value = None, 0
for key, value in fasta_seq.items():
    if calc_cg(value) > max_value:
        max_key = key
        max_value = calc_cg(value)

print(max_key)
print(max_value*100)