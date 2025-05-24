class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def func(temp,left,right):
            if len(temp)==(n*2):
                ans.add(temp)
                return 
            if left<n:
                func(temp+'(',left+1,right)
            if left>right:
                func(temp+')',left,right+1)
        func('',0,0)
        return list(ans)