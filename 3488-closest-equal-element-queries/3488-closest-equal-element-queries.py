class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        freq = defaultdict(list)

        for i,n in enumerate(nums):
            insort(freq[n],i)
        n = len(nums)
        def dist(a,b):
            d = abs(a-b)
            return min(d,n-d)
        ans = []
        for i in queries:
            targ = nums[i]
            pos = freq[targ]
            if len(pos)==1:
                ans.append(-1);continue
            k = bisect_left(pos,i)
            prev = pos[k-1] if k>0 else pos[-1]
            nxt = pos[k+1] if k+1<len(pos) else pos[0]
            ans.append(min(dist(i,prev),dist(i,nxt)))
        return ans