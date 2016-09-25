# Problem

http://www.lintcode.com/en/problem/top-k-frequent-words/

Given a list of words and an integer k, return the top k frequent words in the list.

*Notice*

You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.

**Example**

Given

```
[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
```

for k = ```3```, return ```["code", "lint", "baby"]```.

for k = ```4```, return ```["code", "lint", "baby", "yes"]```

# Thoughts

- Count how many times a word appears. Store in a hash. Key is the word, value is the count. Cannot use count as key because there can be duplicated keys. 
- Use a list of tuples (count, word). Sort the list according to count then word.
- Return the first k tuples from the sorted list.
  
# My Solution

## Solution 1 (Use Python 2, support customized function in sort)

```
def topKFrequentWords(words, k):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    
    p = []
    for key, value in dict.items():
        p.append((value, key))
    
    p.sort(cmp=self.cmp)
    result = []
    for i in range(k):
        result.append(p[i][1])
    
    return result
    
    def cmp(self, a, b):
        if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
            return -1
        elif a[0] == b[0] and a[1] == b[1]:
            return 0
        else:
            return 1
    
```

## Solution 2 (Use Python 3)

```
def topKFrequentWords(words, k):
    score = dict()
    for w in words:
        if w in score:
            score[w] += 1
        else:
            score[w] = 1
    
    p = []
    for word, count in score.items():
        p.append((word, 0 - count))
    
    p.sort(key=lambda x: (x[1], x[0]))
    
    result = []
    for i in range(k):
        result.append(p[i][0])
    
    return result
```

# Reference

