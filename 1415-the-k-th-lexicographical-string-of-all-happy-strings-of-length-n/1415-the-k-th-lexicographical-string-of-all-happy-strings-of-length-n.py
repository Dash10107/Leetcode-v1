class Solution:
    def __init__(self):
        self.ans = ''
    def getHappyString(self, n: int, k: int) -> str:
        self.helper(0, [k], n, ['a', 'b', 'c'], "")
        return self.ans
    def helper(self,i,k,n,chars,s):
        if i == n:
            k[0]-=1
            if k[0]==0:
                self.ans = s
            return
        for char in chars:
            if i == 0 or s[-1]!=char:
                self.helper(i+1,k,n,chars,s+char)
            if k[0]==0:
                return
        
