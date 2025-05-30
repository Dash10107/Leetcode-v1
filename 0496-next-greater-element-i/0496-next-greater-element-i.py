class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = deque([nums2[-1]])
        ans = defaultdict(int)
        ans[nums2[-1]]=-1
        for i in range(len(nums2)-2,-1,-1):
            while st and st[-1]<nums2[i]:
                st.pop()
            if not st:
                st.append(nums2[i])
                ans[nums2[i]]=-1
            else:
                ans[nums2[i]]=st[-1]   
                st.append(nums2[i])
            
        res = []
        for n1 in nums1:
            res.append(ans[n1])
        return res