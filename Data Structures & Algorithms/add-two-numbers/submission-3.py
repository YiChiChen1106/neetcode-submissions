# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        num_1 = 0
        cnt = 0
        while cur:
            num_1 = num_1 + cur.val * 10 ** cnt
            cnt += 1
            cur = cur.next
        
        cur = l2
        num_2 = 0
        cnt = 0
        while cur:
            num_2 = num_2 + cur.val * 10 ** cnt
            cnt += 1
            cur = cur.next
        
        res = num_1 + num_2
        if res == 0:
            dummy = ListNode(0)
            return dummy
        else:
            dummy = ListNode()
            cur = dummy
            while res:
                cur.next = ListNode(res % 10)
                res //= 10
                cur =  cur.next

            return dummy.next



