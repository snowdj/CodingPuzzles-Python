from CodingPuzzles.linkedlist.lib import listnode, list0, list1

list0 = list0.LinkedList0()
list1 = list1.LinkedList1()

def changeList2Num(self, lst):
    arr = []
    while lst:
        arr.append(lst.val)
        lst = lst.next

    num = 0
    for i in range(0, len(arr)):
        num += arr[i] * pow(10, i)
    return num


def changeNum2ReverseList(self, num):
    arr = [int(x) for x in str(num)]
    rarr = arr.reverse()
    dummy = listnode.ListNode(0)
    dhead = dummy
    for i in rarr:
        node = listnode.ListNode(i)
        dummy.next = node
        dummy = dummy.next

    return dhead.next


def addLists(self, l1, l2):
    # write your code here

    if l1:
        n1 = self.changeList2Num(l1)
    else:
        n1 = 0

    if l2:
        n2 = self.changeList2Num(l2)
    else:
        n2 = 0

    sum2 = n1 + n2
    lst = self.changeNum2ReverseList(sum2)
    return lst


if __name__ == '__main__':
    addLists(list0, list1)