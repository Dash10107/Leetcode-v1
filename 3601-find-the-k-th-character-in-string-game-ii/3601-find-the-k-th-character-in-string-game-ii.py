class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations) + 1
        lens = [1] * n
        for i in range(1, n):
            lens[i] = lens[i - 1] * 2
        shifts = 0
        for i in range(n - 1, 0, -1):
            if k > lens[i - 1]:
                k -= lens[i - 1]
                if operations[i - 1] == 1:
                    shifts += 1
        return chr((shifts % 26) + 97)