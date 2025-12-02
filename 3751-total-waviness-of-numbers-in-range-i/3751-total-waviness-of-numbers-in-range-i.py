class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for v in range(num1,num2+1):
            digs = [int(vi) for vi in str(v)]
            for i in range(1,len(digs)-1):
                if digs[i-1]<digs[i]>digs[i+1] or digs[i-1]>digs[i]<digs[i+1]:
                    ans+=1
        return ans