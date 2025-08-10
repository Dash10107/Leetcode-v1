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