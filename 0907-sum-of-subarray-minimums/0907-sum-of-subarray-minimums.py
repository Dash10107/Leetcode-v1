class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        ans = 0;n=len(arr)
        nse,pse = [0]*n,[0]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            nse[i]= st[-1] if st else n
            st.append(i)
        st = []
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            pse[i]=st[-1] if st else -1
            st.append(i)
        for i in range(n):
            left = i-pse[i]
            right = nse[i]-i
            freq = (left*right)
            val = (arr[i]*freq)%mod
            ans  = (ans+val)%mod
        return ans%mod