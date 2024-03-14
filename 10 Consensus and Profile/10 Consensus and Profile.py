import numpy as np

seqs = []
with open("rosalind_cons.txt", "r") as f:
    lines = f.readlines()
    seq = ""
    for line in lines:
        if not line.startswith(">"):
            seq += line.strip()
        else:
            if len(seq) > 0:
                seqs.append(seq)
                seq = ""
    seqs.append(seq)


profile = {'A': np.zeros(len(seqs[0]), dtype=int), 'C': np.zeros(len(seqs[0]), dtype=int),
           'G': np.zeros(len(seqs[0]), dtype=int), 'T': np.zeros(len(seqs[0]), dtype=int)}
for i in range(len(seqs)):
    for j in range(len(seqs[i])):
        profile[seqs[i][j]][j] += 1

consensus_seq = ""
for i in range(len(seqs[0])):
    Max = 0
    acid = ""
    for j in "ACGT":
        if Max < profile[j][i]:
            Max = profile[j][i]
            acid = j
    consensus_seq += acid


# with open("out", "a") as f:
#     std_out = f
#     print(consensus_seq)
#     for key, value in profile.items():
#         print(key+":", " ".join([str(int(x)) for x in value.tolist()]))


print(consensus_seq, file=open("out", "w"))
for key, value in profile.items():
    print(key+":", " ".join([str(x) for x in value.tolist()]), file=open("out", "a"))
