class Solution:
    def maxTotalReward(self, rewards: List[int]) -> int:
        rewards = sorted(set(rewards))
        x  = 1
        for n in rewards:
            valid = x&((1<<n)-1)
            x |= valid<<n
        return x.bit_length()-1