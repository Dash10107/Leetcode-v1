class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        ans = []
        for le in range(2,len(s)+1,1):
            for start in range(0,len(s)-le+1,1):
                temp = s[start:start+le]
                if temp!='':
                    temp = int(temp)
                    if low<=temp<=high:
                        ans.append(temp)
        return ans