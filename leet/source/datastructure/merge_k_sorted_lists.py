class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

from heapq import heappop, heappush
class Solution():
    """use heap"""
    def mergeKLists(self, lists):
        if not lists:
            return None

        trav = dummy = ListNode(-1)
        heap = []
        tie_cnt = 0
        for listhead in lists:
            if listhead:
                self.heappushNode(heap, tie_cnt, listhead)
                tie_cnt += 1

        while heap:
            node = heappop(heap)[2]
            trav.next = node
            trav = trav.next
            if trav.next:
                self.heappushNode(heap, tie_cnt, trav.next)
                tie_cnt += 1

        return dummy.next

    def heappushNode(self, heap, cnt, node):
        heappush(heap, (node.val, cnt, node))

class Solution1():
    def mergeKLists(self, lists):
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        heap = []
        for h in lists:
            while h:
                heappush(heap, h.val)
                h = h.next
        dummy = ListNode(None)
        h = dummy
        while heap:
            h.next = ListNode(heappop(heap))
            h = h.next
        return dummy.next

class Solution2():
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        self.heap = [[i, lists[i].val] for i in range(len(lists)) if lists[i] != None]
        self.hsize = len(self.heap)
        for i in range(self.hsize - 1, -1, -1):
            self.adjustdown(i)
        nHead = ListNode(0)
        head = nHead
        while self.hsize > 0:
            ind, val = self.heap[0][0], self.heap[0][1]
            head.next = lists[ind]
            head = head.next
            lists[ind] = lists[ind].next
            if lists[ind] is None:
                self.heap[0] = self.heap[self.hsize-1]
                self.hsize = self.hsize - 1
            else:
                self.heap[0] = [ind, lists[ind].val]
            self.adjustdown(0)
        return nHead.next

    def adjustdown(self, p):
        lc = lambda x: (x + 1) * 2 - 1
        rc = lambda x: (x + 1) * 2
        while True:
            np, pv = p, self.heap[p][1]
            if lc(p) < self.hsize and self.heap[lc(p)][1] < pv:
                np, pv = lc(p), self.heap[lc(p)][1]
            if rc(p) < self.hsize and self.heap[rc(p)][1] < pv:
                np = rc(p)
            if np == p:
                break
            else:
                self.heap[np], self.heap[p] = self.heap[p], self.heap[np]
                p = np

class Solution3():
    """divide and conquer"""
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(None)
        h = dummy
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        if left:
            h.next = left
        if right:
            h.next = right
        return dummy.next
