# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            kth = prev
            for i in  range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            cur = prev.next
            prev_node = group_next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev_node
                prev_node = cur
                cur = tmp
            tmp = prev.next
            prev.next = kth
            prev = tmp
        

        