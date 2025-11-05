class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        s  = sum(nums);ans=0
        if target>s:return -1
        nums = list(map(lambda x:-x,nums))
        heapify(nums)
        while target:
            n = -heappop(nums)
            s-=n
            if s<target<n:
                ans+=1
                s+=n
                heappush(nums,-n//2)
                heappush(nums,-n//2)
            target-= n*(n<=target)
        return ans