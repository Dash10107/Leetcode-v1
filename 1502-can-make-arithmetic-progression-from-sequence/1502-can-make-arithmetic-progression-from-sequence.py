class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = -1
        for i in range(1,len(arr)):
            if diff==-1:
                diff=arr[i]-arr[i-1]
            elif arr[i]-arr[i-1]!=diff:
                return False
        return True