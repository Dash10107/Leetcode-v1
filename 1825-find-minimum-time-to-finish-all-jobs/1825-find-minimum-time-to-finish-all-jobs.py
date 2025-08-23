class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        arr =[0]*k
        self.ans =float('inf')
        def func(i):
            if i==n:
                self.ans = min(self.ans,max(arr)) 
                return
            if max(arr)>=self.ans:
                return 
            for j in range(k):
                arr[j]+=jobs[i]
                func(i+1)
                arr[j]-=jobs[i]
                if arr[j]==0:
                    break
        func(0)
        return self.ans