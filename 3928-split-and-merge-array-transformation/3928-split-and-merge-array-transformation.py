class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        t1 = tuple(nums1);t2=tuple(nums2)
        q = deque([t1]);st= set();st.add(t1)
        ans = 0;n=len(nums1)
        while q:
            nn = len(q)
            for _ in range(nn):
                state =  q.popleft()
                if state==t2:return ans
                for l in range(n):
                    for r in range(l,n):
                        rem = state[l:r+1]
                        left = state[:l];right = state[r+1:]
                        comb = left+right
                        for i in range(len(comb)+1):
                            nt = comb[:i]+rem+comb[i:]
                            if nt not in st:
                                q.append(nt)
                                st.add(nt)
            ans+=1