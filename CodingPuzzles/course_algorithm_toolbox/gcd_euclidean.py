# Uses python3
import sys

def gcd_euclid(a, b):
    if b == 0:
        return a

    r_a = a % b
    return gcd_euclid(b, r_a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a < b:
        a, b = b, a
    print(gcd_euclid(a, b))