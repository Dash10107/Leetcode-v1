class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.arr= []
        n =len(s)
        def permut(i,st):
            if i==n:
                self.arr.append(st)
                return
            permut(i+1,st+s[i])
            if  s[i].isalpha():
                permut(i+1,st+ s[i].swapcase())
            return
        permut(0,'')
        return self.arr