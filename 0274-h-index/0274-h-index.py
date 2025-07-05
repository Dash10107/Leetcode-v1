class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)
        for i,c in enumerate(citations):
            if c>= (n-i):
                h = max(h,n-i)
        return h