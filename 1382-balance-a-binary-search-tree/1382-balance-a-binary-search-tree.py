# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        nums= inorder(root)
        def bst(arr):
            if not arr:return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left=bst(arr[:mid])
            root.right=bst(arr[mid+1:])
            return root
        return bst(nums)
