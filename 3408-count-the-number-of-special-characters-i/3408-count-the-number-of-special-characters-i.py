class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        ans=0
        for ch in s:
            if ch.islower() and ch.upper() in s:
                ans+=1
        return ans