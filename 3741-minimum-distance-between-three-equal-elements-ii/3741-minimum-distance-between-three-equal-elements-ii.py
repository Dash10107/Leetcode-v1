class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        c = defaultdict(list)
        for i,n in enumerate(nums):
            c[n].append(i)
        ans = float('inf')
        for key in c:
            if len(c[key])>=3:
                for i in range(len(c[key])-2):
                    ans = min(ans,2*(c[key][i+2]-c[key][i]))
        return ans if ans!=float('inf') else -1