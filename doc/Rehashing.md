# Problem

http://www.lintcode.com/en/problem/rehashing/

The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

size=3, capacity=4

```
[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
```

The hash function is:

```
int hashcode(int key, int capacity) {
    return key % capacity;
}
```

here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

```
index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
```

Given the original hash table, return the new hash table after rehashing.

*Notice*

For negative integer in hash table, the position can be calculated as follow:

C++/Java: if you directly calculate -4 % 3 you will get -1. You can use function: a % b = (a % b + b) % b to make it is a non negative integer.

Python: you can directly use -1 % 3, you will get 2 automatically.

# Thoughts

只需要按照重哈希的原理来做。
重哈希，就是在新的容量的哈希表中放置元素。
拉链法，如果一个位置上已经有元素了，就把新的元素放在linkedlist的最后。

解法：
首先计算得新的size
初始化新的hashtable (in the end, return this new hashtable).

对于原来hashtable中的每一个元素（实际上，是用linkedlist实现的）
计算这个元素在新的hashtable中的index: index = start.val % new_size (注意什么是start.val 因为是linkedlist中的元素)
temp = newHashtable[index] -- 可能不是空的
如果temp已经存在，找到linkedlist末尾
最后找到了，就赋值给这个新的结尾：temp.next = ListNode(start.val)

如果temp不存在，就直接放：newHashtable[index] = ListNode(start.val)

最后不要忘记把start向后面移动 start = start.next

# My Solution

```
def rehashing(hashtable):
    if not hashtable:
        return
    
    oldSize = len(hashtable)
    newSize = oldSize * 2
    newHashtable = [None for i in range(newSize)]
    
    for start in hashtable:
        while start != None:
            index = start.val % newSize
            temp = newHashtable[index]
            if temp:
                while temp and temp.next:
                    temp = temp.next
                temp.next = ListNode(start.val)
            else:
                newHashtable[index] = ListNode(start.val)
            
            start = start.next
    
    return newHashtable
```

