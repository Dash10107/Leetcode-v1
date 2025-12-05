class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        n,mn = len(nums),nums.pop(0)
        num1,num2=0,mn
        for num in nums:
            if num<num1:return 0
            if num>num1+num2:
                num1 = num-num2
            num2 = num-num1
            if num2<mn:mn=num2
        return comb(n+mn,mn)%mod