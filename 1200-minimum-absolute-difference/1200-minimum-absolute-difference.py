class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        mndiff = float('inf')
        for i in range(1,len(arr)):
            temp = arr[i]-arr[i-1]
            if temp<mndiff:
                mndiff = temp 
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==mndiff:
                ans.append((arr[i-1],arr[i]))
        return ans