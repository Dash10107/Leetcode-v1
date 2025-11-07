class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr=[0]*(102)
        for s,e in nums:
            arr[s]+=1
            arr[e+1]-=1
        ans=0
        for i in range(1,102):
            arr[i]+=arr[i-1]
            if arr[i]!=0:ans+=1
        return ans