class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0;n=len(arr)
        xa,xb = 0,0
        for i in range(n):
            xa =0
            for j in range(i+1,n):
                xa ^= arr[j-1]
                xb = 0
                for k in range(j,n):
                    xb ^= arr[k]
                    if xa==xb:ans+=1
        return ans