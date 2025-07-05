class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = -1
        for ch in c:
            if c[ch]==ch:
                ans = max(ch,ans)
        return ans