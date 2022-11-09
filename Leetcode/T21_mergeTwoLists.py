"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
"""

from Tools.listNode import ListNode, transform


def mergeTwoLists(l1: ListNode, l2: ListNode):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    elif l2.val < l1.val:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def mergeTwoLists2(l1, l2):
    prehead = ListNode(-1)
    curr = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l2 if l1 is None else l1
    return prehead.next


l1 = transform([1, 2, 4])
l2 = transform([1, 3, 4])
print(mergeTwoLists(l1, l2))

l1 = transform([1, 2, 4])
l2 = transform([1, 3, 4])
print(mergeTwoLists2(l1, l2))
