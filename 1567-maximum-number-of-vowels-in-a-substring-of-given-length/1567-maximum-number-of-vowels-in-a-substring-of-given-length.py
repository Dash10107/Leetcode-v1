class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set('aeiou')
        cnt =0;ans=0
        for j in range(k):
            if s[j] in vowels:
                cnt+=1
        l = 0
        ans = cnt
        for i in range(k,len(s)):

            if s[l] in vowels:
                cnt-=1
            l+=1
            if s[i] in vowels:
                cnt+=1
            ans = max(ans,cnt)
        return ans
            
            