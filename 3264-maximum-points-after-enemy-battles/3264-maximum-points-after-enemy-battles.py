class Solution:
    def maximumPoints(self, enemy: List[int], curr: int) -> int:
        m = min(enemy);s = sum(enemy)
        n = len(enemy);p = -(n-1)
        if curr<m:
            return 0
        curr+= s-m
        return curr//m