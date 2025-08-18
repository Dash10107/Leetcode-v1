class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)
        dp = {}
        def func(i,prev):
            if i==n:return 0
            if (i,prev) in dp:return dp[(i,prev)]
            ans = float('inf')/2
            idd = bisect_right(arr2,prev)
            if arr1[i]>prev:
                ans = min(ans,func(i+1,arr1[i]))
            if idd<len(arr2):
                ans = min(ans,func(i+1,arr2[idd])+1)
            dp[(i,prev)]=ans
            return ans
        ans =  func(0,float('-inf'))
        return ans if ans!=float('inf') else -1