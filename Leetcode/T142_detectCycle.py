"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
"""
import Tools.listNode as tl

def detectCycle(head: tl.ListNode):
    dict = {}
    prev = None
    curr = head
    while curr:
        if curr not in dict:
            dict[curr] = prev
            curr = curr.next
        else:
            return curr
    return None


