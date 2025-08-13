# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: ListNode) -> ListNode:
            prev = None
            curr = head

            while curr is not None:
                next_node = curr.next  
                curr.next = prev      
                prev = curr           
                curr = next_node      
            return prev
        r1,r2 = reverse(l1),reverse(l2)
        dummy = ListNode()
        head = dummy
        carry= 0
        while r1 or r2:
            t = (r1.val if r1 else 0)
            s = (r2.val if r2 else 0)
            p = s + t + carry

            carry = p // 10
            head.next = ListNode(p % 10)  # store only the digit
            head = head.next

            r1 = (r1.next if r1 else None)
            r2 = (r2.next if r2 else None)

        # handle remaining carry
        if carry:
            head.next = ListNode(carry)

        return reverse(dummy.next)