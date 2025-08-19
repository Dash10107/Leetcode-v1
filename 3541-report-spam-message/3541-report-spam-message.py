class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        c = 0
        s = set(bannedWords)
        for m in message:
            if m in s:c+=1
            if c==2:break
        return c==2