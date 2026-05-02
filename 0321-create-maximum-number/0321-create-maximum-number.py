class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getsingle(nums,l):
            extra = len(nums)-l
            st = []
            for num in nums:
                while st and extra and st[-1]<num:
                    st.pop()
                    extra-=1
                st.append(num)
            return st[:l]
        def merge(arr1,arr2):
            res=[]
            while arr1 or arr2:
                if arr1>arr2:res.append(arr1.pop(0))
                else:res.append(arr2.pop(0))
            return res
        start = max(0,k-len(nums2))
        end = min(k,len(nums1))
        ans = []
        for i in range(start,end+1):
            seq1 = getsingle(nums1,i)
            seq2=getsingle(nums2,k-i)
            cand = merge(seq1,seq2)
            ans=max(ans,cand)
        return ans