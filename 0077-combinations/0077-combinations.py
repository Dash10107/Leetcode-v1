class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1,n+1))
        ans = []
        def func(i,temp):
            if i==n:
                if len(temp)==k:
                    ans.append(temp)
                temp = []
                return
            func(i+1,temp)
            func(i+1,temp+[arr[i]])
        func(0,[])
        return ans