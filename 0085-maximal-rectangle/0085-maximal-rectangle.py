class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights);st = [-1]
        left,right = [0]*n,[0]*n
        ans = 0
        for i in range(n):
            id = st[-1]
            while id!=-1  and heights[i]<= heights[id]:
                st.pop()
                id = st[-1]
            st.append(i)
            left[i]=id
        st = [n]
        for i in range(n-1,-1,-1):
            id = st[-1]
            while id!=n and heights[i]<=heights[id]:
                st.pop()
                id = st[-1]
            st.append(i)
            right[i]=id
            ans = max(ans,heights[i]*(right[i]-left[i]-1))
        return ans
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0;heights = [0]*m
        for j in range(m):heights[j] = int(matrix[0][j])
        for i in range(n):
            for j in range(m):
                if i==0:continue
                if matrix[i][j]=='0':heights[j]=0
                heights[j]+= int(matrix[i][j])
            ans = max(ans,self.largestRectangleArea(heights))
        return ans