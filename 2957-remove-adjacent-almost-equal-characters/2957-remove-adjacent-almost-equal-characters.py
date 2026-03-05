class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ans = 0
        cur = 0
        for i in range(1, len(word)):
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                cur += 1
            else:
                ans += (cur+1)//2
                cur = 0
        ans += (cur+1)//2
        return ans