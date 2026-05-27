# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = 0, 0
        s1, s2 = "", ""

        cur, prev = l1.next, l1
        prev.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        p = prev
        while p:
            s1 += str(p.val)
            p = p.next
        
        cur, prev = l2.next, l2
        prev.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        p = prev
        while p:
            s2 += str(p.val)
            p = p.next
    
        res = int(s1) + int(s2)

        if res == 0:
            return ListNode(0)
        dummy = node = ListNode()

        while res:
            digit = res % 10
            node.next = ListNode(digit)
            res = res // 10
            node = node.next
        node = None
        return dummy.next
        
        
