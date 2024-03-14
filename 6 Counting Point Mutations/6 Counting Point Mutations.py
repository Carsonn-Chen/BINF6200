seq1 = input()
seq2 = input()
count = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        count += 1
print(count)