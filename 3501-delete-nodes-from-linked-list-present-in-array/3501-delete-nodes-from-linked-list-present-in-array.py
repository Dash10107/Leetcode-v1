# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        ans = ListNode()
        prev = ans
        ans.next=head
        prev = ans
        curr = head
        while curr:
            if curr.val in s:prev.next=curr.next
            else:prev=curr
            curr=curr.next
        return ans.next