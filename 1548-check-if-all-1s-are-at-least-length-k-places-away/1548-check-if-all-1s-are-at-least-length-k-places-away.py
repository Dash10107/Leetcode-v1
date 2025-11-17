class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr=0;first=True
        for n in nums:
            if n==1 and first:
                first=False
                curr=0
                continue
            elif n==1:
                if curr<k:return False
                curr=0
            else:curr+=1
            print(curr)
        return True