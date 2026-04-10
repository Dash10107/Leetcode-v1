class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # c = defaultdict(list)
        # for i,n in enumerate(nums):
        #     c[n].append(i)
        ans = float('inf')
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[j]==nums[k]:
                        ans = min(ans,(j-i)+(k-j)+(k-i))
        return ans if ans!=float('inf') else -1