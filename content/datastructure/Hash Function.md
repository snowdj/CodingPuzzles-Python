# Problem

http://www.lintcode.com/en/problem/hash-function/

In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:

```
hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE 

                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

                              = 3595978 % HASH_SIZE
```

here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 0 ~ HASH_SIZE-1).

Given a string as a key and the size of hash table, return the hash value of this key.f

# Thoughts

- The problem provides the function to calculate the hash value. The key to solve this problem is finding an efficient way to calculate.

# My Solution

## Slow solution

```
    def hashCode(key, HASH_SIZE):
        # write your code here
        code = 0

        if len(key) == 0 or HASH_SIZE == 0:
            return ''

        for i in range(len(key)):
            code += ord(key[i]) * 33 ** (len(key) - i - 1)

        code %= HASH_SIZE

        return code
```

## Fast solution

```
    def hashCode(key, HASH_SIZE):
        # write your code here
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans
```