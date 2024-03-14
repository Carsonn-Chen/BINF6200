with open("rosalind_iev.txt", "r") as f:
    num = [int(x) for x in f.readline().strip().split()]

# print(num)

sum = 2 * (num[0] + num[1] + num[2] + 0.75 * num[3] + 0.5 * num[4])
print(sum)