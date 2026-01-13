"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        temp = head
        while temp:
            new = Node(temp.val)
            new.next = temp.next
            save = temp.next
            temp.next = new
            temp = save
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp = head
        ans = head.next
        while temp:
            copy = temp.next
            temp.next = copy.next
            copy.next = copy.next.next if copy.next else None
            temp = temp.next
        return ans