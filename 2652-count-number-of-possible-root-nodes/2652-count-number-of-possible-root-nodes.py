from collections import defaultdict

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        guess = set(map(tuple, guesses))
        root_correct = 0

        def dfs(u, parent):
            nonlocal root_correct
            for v in graph[u]:
                if v == parent:
                    continue
                if (u, v) in guess:
                    root_correct += 1
                dfs(v, u)
        
        dfs(0, -1)
        
        ans = 0
        
        def reroot(u, parent, correct):
            nonlocal ans
            if correct >= k:
                ans += 1
            for v in graph[u]:
                if v == parent:
                    continue
                new_correct = correct
              
                if (u, v) in guess:
                    new_correct -= 1 
                if (v, u) in guess:
                    new_correct += 1  
                reroot(v, u, new_correct)
        
        reroot(0, -1, root_correct)
        return ans
