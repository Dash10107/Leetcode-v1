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
        reverse = False
        while queue:
            tempList = []
            l = len(queue)
            for i in range(l):
                if not  reverse:
                    node = queue.popleft() 
                    tempList.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right) 
                else : 
                    node = queue.pop() 
                    tempList.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)                     
                    if node.left:
                        queue.appendleft(node.left)



            reverse  = not reverse 
            levels.append(tempList)
        
        return levels
        