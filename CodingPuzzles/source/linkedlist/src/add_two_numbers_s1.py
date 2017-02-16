import os, sys

bin_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.abspath(os.path.join(bin_path, '../lib'))
sys.path.append(lib_path)

from CodingPuzzles.source.linkedlist.lib.listnode import ListNode
from CodingPuzzles.source.linkedlist.lib.list0 import LinkedList0
from CodingPuzzles.source.linkedlist.lib.list1 import LinkedList1

list0 = LinkedList0()
list1 = LinkedList1()

def changeList2Num(lst):
    arr = []
    thead = lst.head
    while thead:
        arr.append(thead.val)
        thead = thead.next

    num = 0
    for i, n in enumerate(arr):
        num += arr[i] * pow(10, i)
    return num


def changeNum2ReverseList(num):
    arr = [int(x) for x in str(num)]
    arr.reverse()
    dummy = ListNode(0)
    dhead = dummy
    for i in arr:
        node = ListNode(i)
        dummy.next = node
        dummy = dummy.next

    return dhead.next


def addLists(l1, l2):
    if l1:
        n1 = changeList2Num(l1)
    else:
        n1 = 0

    if l2:
        n2 = changeList2Num(l2)
    else:
        n2 = 0

    sum2 = n1 + n2
    lst = changeNum2ReverseList(sum2)
    return lst


if __name__ == '__main__':
    addLists(list0, list1)
