class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        masoFar,misoFar= arr[0],arr[0]
        res = arr[0]
        for i in range(1,len(arr)):
            curr = arr[i]
            temp = max(curr,curr*misoFar,curr*masoFar)
            misoFar = min(curr,curr*misoFar,curr*masoFar)
            masoFar = temp
            res = max(res,temp)
        return res        