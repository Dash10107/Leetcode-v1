class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = set()
        for ch in s:
            if ch in dic:
                return ch
            else:
                dic.add(ch)
        