class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        s = sorted(c,reverse=True,key=lambda x:c[x])
        return s[:k]
        