class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        ans = 0
        mid = False
        for i in c:
            c1,c2= tuple(i)
            
            if str(c2+c1) in c:
                temp = min(c[i],c[c2+c1])
                ans+= temp*4
                c[i]-=temp
                c[c2+c1]-=temp
            if c1==c2:
                p = c[i]//2
                ans+= p*4
                c[i]-= p*2
                if c[i]>0:
                    mid=True
        if mid:
            ans+=2
            
        return ans