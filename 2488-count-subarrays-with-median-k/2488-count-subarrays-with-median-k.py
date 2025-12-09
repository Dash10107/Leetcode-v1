class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ind = nums.index(k)
        ans,diff=0,0
        d[0]=1
        for i,n in enumerate(nums):
            diff+= (n>k)-(n<k)
            if i<ind:d[diff]+=1
            else:
                ans+=(d[diff]+d[diff-1])
        return ans