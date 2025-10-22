class Solution:
    def maxFrequency(self, nums: List[int], k: int, num_ops: int) -> int:
        items = sorted(collections.Counter(nums).items(), key=lambda x: x[0])
        
        # Mode element is present in nums
        max_freq = total_cnt = items[0][1]
        left = right = 0
        for i, (num, cnt) in enumerate(items):
            while right + 1 < len(items) and num + k >= items[right + 1][0]:
                right += 1
                total_cnt += items[right][1]
            while left < i and items[left][0] + k < num:
                total_cnt -= items[left][1]
                left += 1
            max_freq = max(max_freq, cnt + min(num_ops, total_cnt - cnt))

        total_cnt = items[0][1]
        right = 0
        for i, (num, cnt) in enumerate(items):
            while right + 1 < len(items) and num + 2 * k >= items[right + 1][0]:
                right += 1
                total_cnt += items[right][1]
            max_freq = max(max_freq, min(num_ops, total_cnt))
            total_cnt -= cnt

        return max_freq