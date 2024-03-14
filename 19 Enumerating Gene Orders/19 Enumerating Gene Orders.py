import numpy as np
import math

def permute(nums):

    visit = [True for _ in range(len(nums))]
    tmp = nums[:]

    def dfs(position):
        if position == len(nums):
            res.append(tmp[:])
            return

        for index in range(0, len(nums)):
            if visit[index]:
                tmp[position] = nums[index]
                visit[index] = False
                dfs(position + 1)
                visit[index] = True

    res = []
    dfs(0)
    return res


n = 7
l = np.arange(1, n+1).tolist()
# print(l)
ans = permute(l)
print(math.factorial(n))
for i in ans:
    print(' '.join(str(x) for x in i))

