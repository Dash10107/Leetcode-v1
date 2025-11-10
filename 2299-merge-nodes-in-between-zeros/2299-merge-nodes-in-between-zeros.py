# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        root = head.next
        ans  =  ListNode()
        dummy.next = ans
        while root:
            temp = 0
            while root.val!=0:
                temp+=root.val
                root = root.next
            
            l = ListNode(temp)
            ans.next = l
            ans = ans.next
            root = root.next
        return dummy.next.next            