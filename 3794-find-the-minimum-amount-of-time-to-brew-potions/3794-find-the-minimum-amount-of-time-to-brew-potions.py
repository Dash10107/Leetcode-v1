class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        for i in range(len(mana)):  # Iterate over each potion
            if i == 0:  # First potion
                start = 0
                prev = []
                currS = 0
                for s in skill:  # Compute completion times for potion 0
                    currS += s * mana[i]
                    prev.append(currS)
            else:  # Subsequent potions
                curr = []
                currS = 0
                for s in skill:  # Compute relative completion times for current potion
                    currS += s * mana[i]
                    curr.append(currS)
                nextStart = prev[0]  # Initial start time based on wizard 0
                for j in range(1, len(prev)):  # Adjust start time based on other wizards
                    nextStart = max(nextStart, prev[j] - curr[j-1])
                for k in range(len(prev)):  # Update completion times with new start
                    prev[k] = curr[k] + nextStart
        return prev[-1]