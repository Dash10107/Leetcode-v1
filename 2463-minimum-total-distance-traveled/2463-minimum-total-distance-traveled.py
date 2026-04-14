class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort();factory.sort()
        n = len(robot)
        facs = []
        for pos,c in factory:
            for i in range(c):facs.append(pos)
        m = len(facs)
        dp = [[float('inf')]*(m+1) for i in range(n+1)]
        dp[0][0]=0
        for j in range(m):
            dp[0][j+1]=0
        for i in range(n+1):
            for j in range(m):
                dp[i][j+1]=min(dp[i][j+1],dp[i][j])
                if i<n:
                    t= abs(robot[i]-facs[j])
                    dp[i+1][j+1]=min(dp[i+1][j+1],t+dp[i][j])
        return dp[n][m]