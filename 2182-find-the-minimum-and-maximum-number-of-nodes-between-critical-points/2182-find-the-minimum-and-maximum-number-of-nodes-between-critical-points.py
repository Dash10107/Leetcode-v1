# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head;nextt=head.next
        i=2;cs=[]
        while nextt.next:
            if nextt.val<prev.val and nextt.val<nextt.next.val:
                cs.append(i)
            elif prev.val<nextt.val and nextt.next.val<nextt.val:
                cs.append(i)
            i+=1
            prev=nextt
            nextt=nextt.next
        if len(cs)<=1:
            return [-1,-1]
        else:
            ma=cs[-1]-cs[0]
            mi=min(cs[j+1]-cs[j] for j in range(len(cs)-1))
            return [mi,ma]