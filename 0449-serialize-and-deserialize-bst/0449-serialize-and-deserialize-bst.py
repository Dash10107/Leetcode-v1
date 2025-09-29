# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if root is None:
            return 'n'    
        left = self.serialize(root.left) 
        right = self.serialize(root.right)
        return str(root.val)+','+left+','+right
        """Encodes a tree to a single string.
        """
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        self.i = 0
        def dfs():
            if arr[self.i]=='n':
                self.i+=1
                return None
            node = TreeNode(int(arr[self.i]))
            self.i+=1
            node.left =dfs()
            node.right=dfs()
            return node
        return dfs()

        
        """Decodes your encoded data to tree.
        """
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans