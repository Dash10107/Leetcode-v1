# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        levels = []
        reverse = True
        while queue:
            tempList = []
            l = len(queue)
            for i in range(l):
                node = queue.pop() 
                tempList.append(node.val)
                if node.right:
                    queue.appendleft(node.right)                     
                if node.left:
                    queue.appendleft(node.left)
            if reverse:levels.append(tempList[::-1])
            else:levels.append(tempList)
            reverse = not reverse
        return levels
        