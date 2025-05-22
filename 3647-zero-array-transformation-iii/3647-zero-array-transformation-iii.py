class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)

        # Create a list to store all end indices for queries starting at each index
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)  # Store 'r' for every 'l' in the query

        avail = []   # Max-heap (using negatives) to store available end points of intervals
        active = []  # Min-heap to store end points of currently selected intervals
        chosen = 0   # Count of intervals chosen so far

        # Traverse each index of the nums array
        for i in range(n):

            # Add all queries that start at index i to the available heap
            for r in starts[i]:
                heapq.heappush(avail, -r)  # Use negative to simulate max-heap

            # Remove any active intervals that have already ended before or at i
            while active and active[0] < i:
                heapq.heappop(active)

            # Determine how many more intervals are needed to satisfy nums[i]
            need = nums[i] - len(active)

            # Try to satisfy the need by selecting from available intervals
            for _ in range(need):
                # Remove intervals from avail that have already ended
                while avail and -avail[0] < i:
                    heapq.heappop(avail)
                # If not enough intervals available, return -1 (impossible)
                if not avail:
                    return -1
                # Choose the interval with farthest end (max-heap behavior)
                r = -heapq.heappop(avail)
                heapq.heappush(active, r)  # Add it to active set
                chosen += 1  # Increase count of intervals used

        return q - chosen