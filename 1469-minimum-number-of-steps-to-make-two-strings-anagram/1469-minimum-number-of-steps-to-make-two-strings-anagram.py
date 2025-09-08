class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = c1-Counter(t)
        return sum(c2.values())