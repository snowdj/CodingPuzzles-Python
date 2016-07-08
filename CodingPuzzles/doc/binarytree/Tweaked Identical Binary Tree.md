# Problem

Check two given binary trees are identical or not. Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one node in the tree.

Example

```
    1            1
   / \          / \
  2   3   and  3   2
 /                  \
4                    4
```
are identical.

# Thoughts

- Recursive
- Check node from tree a, and node from tree b. If the node differs, then return False
- If the node is the same, check the following two conditions:
  - a's left == b's left && a's right == b's right
  - a's left == b's right && a's right == b's left

# My Solution

```
    def isTweakedIdentical(self, a, b):
        # Write your code here
        if a == None and b == None:
            return True

        if a and b and a.val == b.val:
            return self.isTweakedIdentical(a.left, b.left) and \
                    self.isTweakedIdentical(a.right, b.right) or \
                    self.isTweakedIdentical(a.left, b.right) and \
                    self.isTweakedIdentical(a.right, b.left)

        return False
```

# Reference
