# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        node = head
        while node:
            temp += [node.val]
            node = node.next
        temp.sort()
        res = root = ListNode(0)
        for i in temp:
            t  = ListNode(i)
            root.next = t
            root  = root.next
        return res.next
