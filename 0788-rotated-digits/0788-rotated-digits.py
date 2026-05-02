class Solution:
    def rotatedDigits(self, n: int) -> int:
        neut={'0','1','8'}
        transform = {'2','5','6','9'}
        invalid = {'3','4','7'}
        def check(x):
            trans=False
            for ch in x:
                if ch in invalid:return False
                if ch in transform:trans=True
            return trans
        ans=0
        for i in range(1,n+1):
            if check(str(i)):ans+=1
        return ans