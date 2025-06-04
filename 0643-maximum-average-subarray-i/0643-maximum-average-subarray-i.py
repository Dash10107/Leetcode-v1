class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        temp = 0
        ans = float('-inf')
        j=0
        for i in range(len(arr)):
            temp += arr[i]
            if  i-j+1==k:
                ans = max(ans,temp)
                temp-=arr[j]
                j+=1
        return ans/k
