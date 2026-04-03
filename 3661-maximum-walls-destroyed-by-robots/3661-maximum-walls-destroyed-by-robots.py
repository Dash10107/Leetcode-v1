class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Preprocess: deduplicate walls and sort robots by position
        walls = sorted(set(walls))
        bots = sorted(zip(robots, distance))
        n = len(bots)
        
        if n == 0 or not walls:
            return 0
        
        # Calculate attack intervals for each robot
        left_intervals = []
        right_intervals = []
        
        for i, (pos, dist) in enumerate(bots):
            left_boundary = bots[i-1][0] + 1 if i > 0 else float('-inf')
            right_boundary = bots[i+1][0] - 1 if i < n-1 else float('inf')
            
            # Left attack interval: [max(pos-dist, left_boundary), pos]
            left_intervals.append((max(pos - dist, left_boundary), pos))
            
            # Right attack interval: [pos, min(pos+dist, right_boundary)]
            right_intervals.append((pos, min(pos + dist, right_boundary)))
        
        def count_walls(start: int, end: int) -> int:
            if start > end:
                return 0
            return bisect_right(walls, end) - bisect_left(walls, start)
        
        def get_overlap(interval1: tuple, interval2: tuple) -> int:
            start = max(interval1[0], interval2[0])
            end = min(interval1[1], interval2[1])
            return count_walls(start, end) if start <= end else 0
        
        # Calculate walls count for each interval
        left_counts = [count_walls(start, end) for start, end in left_intervals]
        right_counts = [count_walls(start, end) for start, end in right_intervals]
        
        # Dynamic programming: choose left or right for each robot
        dp_left = left_counts[0]
        dp_right = right_counts[0]
        
        for i in range(1, n):
            # Current robot chooses left
            new_left = max(
                dp_left + left_counts[i],  # Previous also chose left
                dp_right + left_counts[i] - get_overlap(left_intervals[i], right_intervals[i-1])
            )
            
            # Current robot chooses right
            new_right = max(
                dp_right + right_counts[i],  # Previous also chose right
                dp_left + right_counts[i] - get_overlap(right_intervals[i], left_intervals[i-1])
            )
            
            dp_left, dp_right = new_left, new_right
        
        return max(dp_left, dp_right)