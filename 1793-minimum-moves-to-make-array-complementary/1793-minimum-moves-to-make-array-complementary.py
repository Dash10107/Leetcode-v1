class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0]*(2*limit+2)
        for i in range(n//2):
            j = n-i-1
            a,b = nums[i],nums[j]
            low = min(a,b);high=max(a,b)
            diff[2]+=2
            diff[low+1]-=1
            diff[high+limit+1]+=1
            diff[a+b]-=1
            diff[a+b+1]+=1
        ans = float('inf');curr=0
        for i in range(2,2*limit+2):
            curr+=diff[i]
            ans=min(ans,curr)
        return ans