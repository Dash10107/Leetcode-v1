class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        inds = []
        for i,n in enumerate(nums):
            if n==key:
                inds.append(i)
        ans = set()
        for i in range(len(nums)):
            for j in inds:
                if abs(j-i)<=k:
                    ans.add(i)
                    continue
        return sorted(list(ans))