class Solution:
    def minProcessingTime(self, proc: List[int], tasks: List[int]) -> int:
        proc.sort()
        tasks.sort(reverse=True)
        i=0;j=0;n=len(proc);m=len(tasks)
        ans=0
        while i<n:
            c=0
            while j<m and c<4:
                ans=max(proc[i]+tasks[j],ans)
                j+=1;c+=1
            i+=1
        return ans