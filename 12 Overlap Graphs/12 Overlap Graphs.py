seqs = {}
with open("rosalind_grph.txt", "r") as f:
    lines = f.readlines()
    seq = ""
    id = lines[0][1:].strip()
    for line in lines:
        if line.startswith(">"):
            if len(seq) > 0:
                seqs[id] = seq
                seq = ""
                id = line[1:].strip()
        else:
            seq += line.strip()
    seqs[id] = seq

print(seqs)

for key, value in seqs.items():
    for key2, value2 in seqs.items():
        if key != key2:
            if value[-3:] == value2[:3]:
                print(key, key2)