def fib(n, k):
    if n == 1 or n == 2:
        return 1
    return fib(n-1, k) + fib(n-2, k)*k


n, k = input().split()
print(fib(int(n), int(k)))
