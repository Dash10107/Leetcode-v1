class Solution:
    def longestPrefix(self, needle: str) -> str:
        lps = [0]*len(needle)
        pre = 0
        for i in range(1,len(needle)):
            while pre>0 and needle[pre]!=needle[i]:
                pre=lps[pre-1]
            if needle[pre]==needle[i]:
                pre+=1
                lps[i]=pre
        return needle[:lps[len(needle)-1]]