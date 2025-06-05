class Solution:
    def longestAlternatingSubarray(self, arr: List[int], thres: int) -> int:
        ans = 0
        i,n = 0,len(arr)
        while i<n:
            if arr[i]%2==0 and arr[i]<=thres:
                lent = 1
                j = i+1
                while j<n and arr[j]<=thres and ((arr[j]%2) != (arr[j-1]%2)):
                    j+=1
                    lent+=1
                ans = max(ans,lent)
                i = j
            else:
                i+=1
        return ans