class Solution:
    def numSubmatrixSumTarget(self, nums: List[List[int]], targ: int) -> int:
        n,m = len(nums),len(nums[0])
        ans=0
        for i in range(n):
            for j in range(1,m):
                nums[i][j]+=nums[i][j-1]
        for cs in range(m):
            for ce in range(cs,m):
                for rs in range(n):
                    s=0
                    for re in range(rs,n):
                        s+= (nums[re][ce]-(nums[re][cs-1] if cs else 0))
                        if s==targ:ans+=1
        return ans