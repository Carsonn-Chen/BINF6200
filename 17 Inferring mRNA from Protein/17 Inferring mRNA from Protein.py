inferring_possibility = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3,
                         'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4, 'stop': 3}
mod = 1000000

ans = 1
with open('rosalind_mrna.txt', 'r') as f:
    seq = ''.join(f.read().split())
# print(seq)

for aa in seq:
    ans = (ans * inferring_possibility[aa]) % mod
ans = (ans * inferring_possibility['stop']) % mod

print(ans)

