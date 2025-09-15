class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(t[0]+t[1] for t in tasks)