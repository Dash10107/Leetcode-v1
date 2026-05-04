class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        m=len(nums);n = len(str(nums[0]))
        ans =0
        for i in range(n):
            dic = defaultdict(int)
            tot=0
            for j in range(m):
                dic[str(nums[j])[i]]+=1
            for dv in dic.values():
                ans+= dv*(m-dv)
        return ans//2