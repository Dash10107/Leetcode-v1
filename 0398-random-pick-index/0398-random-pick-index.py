class Solution:

    def __init__(self, nums: List[int]):
        dic = defaultdict(list)
        for i,n in enumerate(nums):
            dic[n].append(i)
        self.dic=dic
        

    def pick(self, target: int) -> int:
        arr = self.dic[target]
        return arr[randint(0,len(arr)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)