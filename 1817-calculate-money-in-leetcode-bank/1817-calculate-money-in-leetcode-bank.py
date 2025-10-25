class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 1
        i=1;count=1
        for j in range(1,n):
            if j%7==0:
                i+=1
                count=i
                ans+=count
            else:
                count+=1
                ans+=count
        return ans