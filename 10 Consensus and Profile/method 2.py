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
# print(seqs)

new_seq = list(zip(*seqs))
# print(np.shape(seqs))
# print(np.shape(new_seq))
# print(new_seq)

profile = {"A": [], "C": [], "G": [], "T": []}
for seq in new_seq:
    for x in "ACGT":
        profile[x].append(seq.count(x))


consensus_seq = ""
for i in range(len(profile["A"])):
    Max = 0
    acid = ""
    for j in "ACGT":
        if Max < profile[j][i]:
            Max = profile[j][i]
            acid = j
    consensus_seq += acid

print(consensus_seq, file=open("out2", "w"))
for key, value in profile.items():
    print(key+": "+(' '.join(str(x) for x in value)), file=open("out2", "a"))
