import math
with open("rosalind_lia.txt") as f:
    k, n = map(int, f.readline().strip().split())


P = 2**k
probability = 0
for i in range(n, P + 1):
    prob = (math.factorial(P) /
            (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(
                P - i))
    probability += prob
print(probability)
