class Solution:
    def rotatedDigits(self, n: int) -> int:
        neut={0,1,8}
        transform = {2,5,6,9}
        invalid = {3,4,7}
        dp =[0]*(n+1)
        ans=0
        for i in range(n+1):
            if i<10:
                if i in neut:dp[i]=1
                elif i in transform:
                    dp[i]=2
                    ans+=1
            else:
                a=dp[i//10]
                b=dp[i%10]
                if a==1 and b==1:dp[i]=1
                elif a>=1 and b>=1:
                    dp[i]=2;ans+=1
                
        return ans
                