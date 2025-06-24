class Solution:
    def validPalindrome(self, s: str) -> bool:
        def func(a,b):
            while a<b:
                if s[a]==s[b]:
                    a+=1
                    b-=1
                else:
                    return False
            return True
        l,r = 0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                r-=1
                l+=1
            else:
                return func(l+1,r) or func(l,r-1)
        return True
        