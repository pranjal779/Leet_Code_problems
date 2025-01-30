from collections import defaultdict, deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
      
        # Depth-first search function to explore all the nodes within a connected component
        def dfs(node):
            component_nodes.append(node)
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        # Breadth-first search function to calculate the maximum distance from the start node
        def bfs(start_node):
            maximum_distance = 1
            distances = [float('inf')] * (n + 1)
            distances[start_node] = 1
            queue = deque([start_node])
          
            while queue:
                current_node = queue.popleft()
                for neighbor in graph[current_node]:
                    if distances[neighbor] == float('inf'):
                        maximum_distance = distances[neighbor] = distances[current_node] + 1
                        queue.append(neighbor)
          
            # Assign an incremental distance value for disconnected nodes in the component
            for node in component_nodes:
                if distances[node] == float('inf'):
                    maximum_distance += 1
                    distances[node] = maximum_distance
          
            # Verify the resultant distances conform to the problem constraints
            for node in component_nodes:
                for neighbor in graph[node]:
                    if abs(distances[node] - distances[neighbor]) != 1:
                        return -1
            return maximum_distance

        # Initialize an adjacency list graph and visited list
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
      
        visited = [False] * (n + 1)
        total_sets = 0
      
        # Traverse all nodes to find disconnected components
        for i in range(1, n + 1):
            if not visited[i]:
                component_nodes = []
                dfs(i)  # DFS to populate component_nodes
              
                # Perform BFS on all nodes in the component and find the maximum distance
                max_dist = max(bfs(node) for node in component_nodes)
              
                if max_dist == -1:
                    return -1  # Early return if any component doesn't fulfill the requirements
              
                total_sets += max_dist
      
        # Return the total potential magnificent sets across all components
        return total_sets
