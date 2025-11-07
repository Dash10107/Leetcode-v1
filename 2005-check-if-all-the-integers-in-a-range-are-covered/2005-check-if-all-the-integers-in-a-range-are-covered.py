class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [0]*(52)
        for s,e in ranges:
            arr[s]+=1
            arr[e+1]-=1
        for i in range(1,52):
            arr[i]+=arr[i-1]
            if left<=i<=right and arr[i]==0:
                return False
        return True
