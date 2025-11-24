class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr=''
        for i in nums:
            curr+=str(i)
            n = int(curr,2)
            if n%5==0:ans.append(True)
            else:ans.append(False)
        return ans