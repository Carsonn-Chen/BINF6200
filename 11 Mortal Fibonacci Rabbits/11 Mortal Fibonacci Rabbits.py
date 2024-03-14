n, m = map(int, input().split())

f = [1, 1]
for i in range(2, n):
    tmp = f[i - 1] + f[i - 2]
    if i == m:
        tmp = tmp - 1
    if i > m:
        tmp = tmp - f[i - m - 1]
    f.append(tmp)

print(f[-1])