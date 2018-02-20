def fib_rec(x):
    if x is None:
        return None

    if x <= 1:
        return x

    return fib_rec(x-1) + fib_rec(x-2)

if __name__ == "__main__":
    for i in range(6):
        print(fib_rec(i))