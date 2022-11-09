"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
"""

import Tools.listNode as tl

def solution1(head):
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    length = (length + 2) // 2

    curr = head
    for i in range(length - 1):
        curr = curr.next

    return curr

def solution2(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

head = tl.transform([1,2,3,4,5])
print(solution1(head))
print(solution2(head))