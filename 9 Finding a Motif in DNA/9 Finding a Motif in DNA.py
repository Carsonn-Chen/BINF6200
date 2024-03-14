def partial(pattern):
    ret = [0]

    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret


def kmp_search(T, P):

    ppartial, ret, j = partial(P), [], 0

    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = ppartial[j - 1]
        if T[i] == P[j]:
            j += 1
        if j == len(P):
            ret.append(i - (j - 1)+1)
            j = ppartial[j - 1]

    return ret


with open("rosalind_subs.txt", "r") as f:
    seq = f.readline().strip()
    motif = f.readline().strip()

print(seq, motif)

print(" ".join([str(x) for x in kmp_search(seq, motif)]))
# print(kmp_search(seq, motif))