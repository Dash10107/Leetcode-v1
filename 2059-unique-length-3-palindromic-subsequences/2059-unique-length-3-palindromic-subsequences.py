class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):  
            i, j = s.find(c), s.rfind(c)  
            if j > i + 1: 
                res += len(set(s[i+1:j])) 
        return res