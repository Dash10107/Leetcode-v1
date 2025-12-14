class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        st = set('aeiou')
        c = sum(1 if ch in st else 0 for ch in words[0])
        
        ans = (words[0]+' ')
        for word in words[1:]:
            cc = sum(1 if ch in st else 0 for ch in word)
            if cc==c:
                ans+=  (word[::-1]+' ')
            else:ans+= (word+' ')
        ans = ans.rstrip(' ')
        return ans