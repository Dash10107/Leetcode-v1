class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def func(i,j):
            c = 0
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
                c+=1
            return c
        for i in range(len(s)):
            even = func(i,i+1)
            odd = func(i,i)
            ans+=odd+even

        return ans