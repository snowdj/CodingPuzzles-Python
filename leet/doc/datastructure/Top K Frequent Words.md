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

## Solution 3 (Similar to Solution 2)

```
"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    counts = {}
    words = s.split()
    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    count_pairs = []
    for word, cnt in counts.items():
        count_pairs.append((word, cnt))
    
    count_pairs.sort(key=lambda x: (0 - x[1], x[0]))
    
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = []
    for i in range(n):
        top_n.append(count_pairs[i])
    
    return top_n

def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

```

# Reference

