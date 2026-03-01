class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n==1:return [0,0]
        def func(start):
            ans = 0;c=Counter(nums);change=[]
            mx,mn=max(nums),min(nums)
            for i,x in enumerate(nums):
                req = (start+i)%2
                if x%2!=req:
                    ans+=1                
                    if nums[i]==mx:
                        c[nums[i]]-=1
                        c[nums[i]-1]+=1
                        if nums[i]-1<mn:mn=nums[i]-1
                        if c[nums[i]]==0:mx=nums[i]-1
                    elif nums[i]==mn:
                        c[nums[i]]-=1
                        c[nums[i]+1]+=1
                        if nums[i]+1>mx:mn=nums[i]+1
                        if c[nums[i]]==0:mn=nums[i]+1  
            return ans,mx-mn
        m1,a1 = func(0);m2,a2=func(1)
        if m1<m2:
            return [m1,a1]
        elif m2<m1:
            return [m2,a2]
        return [m1,min(a1,a2)]