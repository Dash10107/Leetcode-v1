class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans =0
        def almost(ch,ch2):
            return abs(ord(ch)-ord(ch2))<=1
        i=1
        while i<len(word):
            if almost(word[i],word[i-1]):
                ans+=1
                i+=1
            i+=1
        return ans