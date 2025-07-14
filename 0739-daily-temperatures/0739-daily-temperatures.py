class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        ans = [0]*n
        for i in range(n):
            t = temperatures[i]
            while st and st[-1][1]<t:
                ii,val = st.pop()
                ans[ii]= i-ii
            st.append((i,t))
        return ans