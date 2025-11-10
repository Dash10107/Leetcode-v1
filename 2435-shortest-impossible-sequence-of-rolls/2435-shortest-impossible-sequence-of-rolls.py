class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans = 1
        for i,v in enumerate(rolls):
            seen.add(v)
            if len(seen)==k:
                ans+=1
                seen.clear()
        return ans