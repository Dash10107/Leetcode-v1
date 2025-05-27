class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        odd = False
        temp = ''
        for i in sorted(c.keys()):
            if c[i]&1 and not odd:
                if c[i]>1:
                    ans+= i*((c[i]-1)//2)
                temp = i
                odd = True
            else:
                ans+=i*(c[i]//2)
        ans = ans + temp + ans[::-1]
        return ans