# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    fibs = [1 for i in range(n+1)]
    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n-1]

n = int(input())
print(calc_fib(n))
