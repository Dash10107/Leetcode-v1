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
        arr = defaultdict()
        temp = head
        while temp:
            arr[temp] = Node(temp.val)
            temp= temp.next
        temp= head
        arr[None]=None
        while temp:
            arr[temp].next = arr[temp.next]
            arr[temp].random = arr[temp.random]
            temp = temp.next
        return arr[head]
