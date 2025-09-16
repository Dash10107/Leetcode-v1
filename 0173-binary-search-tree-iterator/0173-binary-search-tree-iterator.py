# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        self.arr = inorder(root)
        self.i=-1;self.n = len(self.arr)

    def next(self) -> int:
        t=self.arr[self.i+1]
        self.i+=1
        return t
        

    def hasNext(self) -> bool:
        return self.i+1<self.n


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()