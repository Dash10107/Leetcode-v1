# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val>root.val:
            head = TreeNode(val)
            head.left = root
            return head
        else:
            root.right = self.insertIntoMaxTree(root.right,val)
            return root