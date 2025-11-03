class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1,m2=0,0
        for n in nums:
            if n==0:continue
            ni = abs(n)
            if ni>m1:m2=m1;m1=ni
            elif m1>=ni and ni>m2:m2=ni
        return m1*m2*100000
