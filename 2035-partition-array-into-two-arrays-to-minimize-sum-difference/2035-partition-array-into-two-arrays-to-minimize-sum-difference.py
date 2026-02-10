class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        s = sum(nums);ans=float('inf')
        n = len(nums)//2
        left = [[] for _ in range(n+1)]
        right = [[] for _ in range(n+1)]
        for mask in range(1<<n):
            sz=0;l=0;r=0
            for i in range(n):
                if (mask & (1<<i)):
                    sz+=1
                    l+=nums[i]
                    r+=nums[i+n]
            left[sz].append(l)
            right[sz].append(r)
        
        for arr in right:
            arr.sort()
        
        for i in range(n+1):
            for a in left[i]:
                b = (s-2*a)//2;rs = n-i
                ind = bisect_left(right[rs],b)
                if ind!=len(right[rs]):
                    ans = min(ans,abs(s-2*(a+right[rs][ind])))
                if ind!=0:
                    ans = min(ans,abs(s-2*(a+right[rs][ind-1])))
        return ans