class Solution:
    def maxScore(self, points: List[int], k: int) -> int:
        n = len(points)
        left = sum(points[:k])
        ans = left;r=n-1;right=0
        for i in range(k-1,-1,-1):
            right+=points[r]
            r-=1
            left-=points[i]
            ans = max(ans,left+right)
        return ans