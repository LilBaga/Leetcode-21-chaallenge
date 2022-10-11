# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=ListNode(0)
        node = n
        sum =0
        while head:
            if head.val == 0:
                if sum!=0:
                    n.next=ListNode(sum)
                    n=n.next
                    sum = 0
            else:
                sum += head.val
                print(sum)
            head= head.next
        return node.next
