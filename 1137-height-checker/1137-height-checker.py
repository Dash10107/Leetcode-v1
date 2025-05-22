class Solution:
    def heightChecker(self, arr: List[int]) -> int:
        temp = sorted(arr)
        ans = 0
        for i in range(len(arr)):
            if arr[i]!=temp[i]:
                ans+=1
        return ans