class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        ans = 0
        for ch in stones:
            if ch in s:ans+=1
        return ans