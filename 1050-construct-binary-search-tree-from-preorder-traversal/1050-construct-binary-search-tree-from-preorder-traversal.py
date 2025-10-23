# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(node,pre):
            if node is None:
                return TreeNode(pre)
            if pre<node.val:
                node.left=insert(node.left,pre)
            elif pre>node.val:
                node.right=insert(node.right,pre)
            return node
        root = None
        for pre in preorder:
            root = insert(root,pre)
        return root