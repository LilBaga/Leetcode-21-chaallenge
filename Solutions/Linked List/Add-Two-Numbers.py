# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        num1 =0 
        pwr=1
        while l1:
            num = l1.val*pwr + num
            l1 = l1.next
            pwr *=10
        print(num)
        pwr=1
        while l2:
            num1 = l2.val*pwr+num1
            l2 = l2.next
            pwr*=10
        num = num1+ num #my number which i want to reverse
        print(num1)
        res = ListNode(0) 
        head = res                          
        while num:  
            digit = num %10
            head.next = ListNode(digit)  
            head = head.next
            num //= 10        
        return res.next or ListNode(0)
