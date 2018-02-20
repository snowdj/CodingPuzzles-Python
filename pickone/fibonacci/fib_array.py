def fib_array(x):
    if x is None:
        return None

    array = [0, 1]
    for i in range(2, x):
        array.append(array[i-1] + array[i-2])

    return array

if __name__ == "__main__":
    result = fib_array(6)
    print(result)
