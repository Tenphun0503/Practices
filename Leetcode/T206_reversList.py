"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
"""

import Tools.listNode as tl

def reverseList(head: tl.ListNode):
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

head = tl.transform([1,2,3,4,5])
print(reverseList(head))