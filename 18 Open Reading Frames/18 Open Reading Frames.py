from Bio import SeqIO

with open("rosalind_orf.txt", "r") as f:
    Seq = SeqIO.read(f, "fasta").seq
    re_Seq = Seq.reverse_complement()


ans = set()
for i in range(0, 3):
    # print(i)
    seq = Seq[i:].translate()
    # print(seq)
    start, stop = [], []
    for pos, aa in enumerate(seq):
        if aa == 'M':
            start.append(pos)
        if aa == '*':
            stop.append(pos)
    # print(start, stop)
    for k in stop:
        for j in start:
            if j < k:
                t = seq[j: k]
                if '*' not in t:
                    ans.add(t)


for i in range(0, 3):
    # print(i)
    seq = re_Seq[i:].translate()
    # print(seq)
    start, stop = [], []
    for pos, aa in enumerate(seq):
        if aa == 'M':
            start.append(pos)
        if aa == '*':
            stop.append(pos)
    # print(start, stop)
    for k in stop:
        for j in start:
            if j < k:
                t = seq[j: k]
                if '*' not in t:
                    ans.add(t)

for x in ans:
    print(x)