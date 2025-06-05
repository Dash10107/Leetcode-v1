class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr = nums[i:j+1]
                gc = reduce(math.gcd,arr)
                lc = reduce(math.lcm,arr)
                prod = math.prod(arr)
                if prod==gc*lc:
                    ans = max(ans,j-i+1)
        return ans