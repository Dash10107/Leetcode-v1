class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            c = Counter(tasks)
            m = max(c.values())
            cm = sum(1 for v in c.values() if v==m)
            empty = ((m-1)*(n+1))+cm
            return max(len(tasks),empty)