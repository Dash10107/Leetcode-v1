# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pre,curr = dummy,head
        while curr and curr.next:
            sec = curr.next 
            nxt = curr.next.next
            sec.next = curr
            curr.next = nxt
            pre.next = sec
            pre = curr
            curr = nxt
        return dummy.next