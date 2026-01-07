class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        c = Counter(arr)
        ans = [0,0]
        curr=1
        while c[curr]>0:
            curr+=1
        ans[1]=curr
        for ch in c:
            if c[ch]==2:
                ans[0]=ch
                break
        return ans