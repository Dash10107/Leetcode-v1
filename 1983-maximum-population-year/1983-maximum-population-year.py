class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0]*101
        year = 0;ma=0
        for b,d in logs:
            arr[b-1950]+=1
            arr[d-1950]-=1
        for i in range(1,100):
            arr[i]+=arr[i-1]
        return arr.index(max(arr))+1950