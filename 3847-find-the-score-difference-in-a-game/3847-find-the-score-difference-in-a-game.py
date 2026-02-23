class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        one,two=0,0
        active=True
        for i,n in enumerate(nums):
            if n%2==1 :
                active = not active
            if (i+1)%6==0:
                active = not active
            if active:one+=n
            else:two+=n
        # print(one,two)
        return one-two