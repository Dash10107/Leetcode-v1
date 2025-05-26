class Solution:
    def average(self, salary: List[int]) -> float:
        s = sum(salary)
        m = min(salary)
        ma = max(salary)
        return ((s-m-ma)/(len(salary)-2))