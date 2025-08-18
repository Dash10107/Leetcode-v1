class Solution:
    def judgePoint24(self, nums: list[int]) -> bool:
        EPS = 1e-6
        
        def dfs(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24) < EPS
            
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if i != j:
                        next_arr = [arr[k] for k in range(len(arr)) if k != i and k != j]
                        for val in (
                            arr[i] + arr[j],
                            arr[i] - arr[j],
                            arr[j] - arr[i],
                            arr[i] * arr[j],
                        ):
                            if dfs(next_arr + [val]):
                                return True
                        if abs(arr[j]) > EPS:
                            if dfs(next_arr + [arr[i] / arr[j]]):
                                return True
                        if abs(arr[i]) > EPS:
                            if dfs(next_arr + [arr[j] / arr[i]]):
                                return True
            return False
        
        return dfs(nums)
