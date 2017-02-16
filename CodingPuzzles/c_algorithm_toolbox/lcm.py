# Uses python3
import sys

def gcd_euclid(a, b):
    if b == 0:
        return a

    r_a = a % b
    return gcd_euclid(b, r_a)

def lcm(a, b):
    if a == b:
        return a
    if a <= 1 or b <= 1:
        return a*b

    gcd = gcd_euclid(a, b)
    return a * b // gcd

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a > b:
        a, b = b, a
    print(lcm(a, b))

