class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        ans  = 1
        dic = defaultdict(int)
        for a in arr:
            dic[a] = 1+ dic[a-diff]
            ans = max(ans,dic[a])
        return ans