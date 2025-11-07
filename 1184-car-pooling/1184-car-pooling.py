class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*1002
        for p,f,t in trips:
            arr[f]+=p
            arr[t]-=p
        ans = 0
        for i in range(1002):
            ans+=arr[i]
            if ans>capacity:return False
        return True