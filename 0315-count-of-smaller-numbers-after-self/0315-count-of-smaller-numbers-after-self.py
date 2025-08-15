class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0]*n
        enum = list(enumerate(nums))
        def merge(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            m = [];i=0;j=0
            while i<len(left) and j<len(right):
                if left[i][1]<=right[j][1]:
                    m.append(left[i])
                    counts[left[i][0]]+=j
                    i+=1
                else:
                    m.append(right[j])
                    j+=1
            while i<len(left):
                m.append(left[i])
                counts[left[i][0]]+=j
                i+=1
            while j<len(right):
                m.append(right[j])
                j+=1
            return m
        merge(enum)
        return counts