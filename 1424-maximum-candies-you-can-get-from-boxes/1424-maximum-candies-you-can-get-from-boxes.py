class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        ans = 0
        rckeys = [False]*len(keys)
        hsbox =[False]*len(containedBoxes)
        opened = [False]*len(keys)
        for box in initialBoxes:
            hsbox[box]=True
            if status[box]==1:
                q.append(box)

        while q:
            node = q.popleft()
            if opened[node]:
                continue
            opened[node]=True
            ans+=candies[node]
            for key in keys[node]:
                if not rckeys[key]:
                    rckeys[key]=True
                    if hsbox[key] and not opened[key]:
                        q.append(key)
            for box in containedBoxes[node]:
                hsbox[box]=True
                if status[box]==1 or rckeys[box]:
                    q.append(box)
        return ans