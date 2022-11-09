class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = [self.val]
        curr = self.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)


def transform(string):
    head = ListNode(-1)
    curr = head
    for i in string:
        curr.next = ListNode(i)
        curr = curr.next
    return head.next