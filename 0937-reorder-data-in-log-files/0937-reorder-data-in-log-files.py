class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def func(log):
            a,b = log.split(' ',1)
            if b[0].isalpha():
                return (0,b,a)
            else:
                return (1,None,None)
        return sorted(logs,key=func)
