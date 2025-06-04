# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode()
        sec = ListNode()
        ans = None
        mid = None
        temp = head
        while temp:
            if temp.val>=x:
                if not mid:
                    mid = temp
                sec.next = temp
                sec = sec.next
            else:
                if not ans:
                    ans = temp
                first.next = temp
                first = first.next
            temp = temp.next
        first.next = mid
        sec.next = None
        return ans if ans else mid

