from typing import List
from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Helper function to find the length of the largest cycle
        def max_cycle(favorites):
            n = len(favorites)
            visited = [False] * n
            max_ans = 0

            # Iterate over all students
            for i in range(n):
                if visited[i]:
                    continue
                cycle = []
                j = i
                # Build the cycle starting from student i
                while not visited[j]:
                    cycle.append(j)
                    visited[j] = True
                    j = favorites[j]

                # Detect the cycle length
                for k, v in enumerate(cycle):
                    if v == j:
                        max_ans = max(max_ans, len(cycle) - k)
                        break
            return max_ans

        # Helper function to perform topological sort and find the longest path in the graph
        def topological_sort(favorites):
            n = len(favorites)
            indegree = [0] * n
            longest_path = [1] * n
            # Create indegree array
            for v in favorites:
                indegree[v] += 1
            # Queue for zero indegree students
            queue = deque([i for i, d in enumerate(indegree) if d == 0])

            # Perform BFS
            while queue:
                current = queue.popleft()
                longest_path[favorites[current]] = max(longest_path[favorites[current]], longest_path[current] + 1)
                indegree[favorites[current]] -= 1
                if indegree[favorites[current]] == 0:
                    queue.append(favorites[current])

            # Sum the distances of mutually favorite pairs
            return sum(longest_path[i] for i, v in enumerate(favorites) if i == favorites[favorites[i]])

        # Return the maximum value among the longest cycle and the result of the topological sort
        return max(max_cycle(favorite), topological_sort(favorite))
