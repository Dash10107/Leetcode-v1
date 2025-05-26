class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr_end = float('-inf')
        chain_len = 0
        for start, end in pairs:
            if start > curr_end:
                chain_len += 1
                curr_end = end
        return chain_len