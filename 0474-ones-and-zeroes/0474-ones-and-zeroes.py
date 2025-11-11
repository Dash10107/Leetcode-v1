class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def func(ind,mi,ni):
            if ind==0:
                zer = strs[ind].count('0')
                ones = len(strs[ind])-zer
                if zer<=mi and ones<=ni:
                    return 1
                else:
                    return 0
            nn =  func(ind-1,mi,ni)
            mm = float('-inf')
            zer = strs[ind].count('0')
            ones = len(strs[ind])-zer
            if zer<=mi and ones<=ni:        
                mm = 1 + func(ind-1,mi-zer,ni-ones)
            return max(nn,mm)
        return func(len(strs)-1,m,n)