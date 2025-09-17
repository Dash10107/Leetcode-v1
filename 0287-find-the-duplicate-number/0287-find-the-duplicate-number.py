class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0;n = len(nums)-1
        for i in range(32):
            mask = 1<<i;b=0;nc = 0
            for j in range(n+1):
                if (j&mask)>0:b+=1
                if (nums[j]&mask)>0:nc+=1
            if nc>b:ans|= mask
        return ans