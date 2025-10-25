class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0]=1
        ans = 1
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])>1:  
                arr[i]= arr[i-1]+1
            ans = max(ans,arr[i])
        return ans
                