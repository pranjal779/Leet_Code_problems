from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Helper function to perform a depth-first-search (dfs) 
        # to determine if a node leads to a cycle (not safe) or not.
        def dfs(node_index):
            # If the node is already visited, return True if it is safe (color 2)
            if node_colors[node_index]:
                return node_colors[node_index] == 2
            # Mark this node as visited (color 1)
            node_colors[node_index] = 1
            # Traverse all connected nodes to see if they lead to a cycle
            for next_node_index in graph[node_index]:
                # If a connected node is not safe, then this node is also not safe
                if not dfs(next_node_index):
                    return False
            # If all connected nodes are safe, mark this node as safe (color 2)
            node_colors[node_index] = 2
            return True

        # Get the number of nodes in the graph
        total_nodes = len(graph)
        # Initialize a list to store the status of the nodes
        # Color 0 means unvisited, 1 means visiting, 2 means safe
        node_colors = [0] * total_nodes
        # Use list comprehension to gather all nodes that are safe after DFS
        # These are the eventual safe nodes that do not lead to any cycles
        safe_nodes = [node_index for node_index in range(total_nodes) if dfs(node_index)]
        return safe_nodes
