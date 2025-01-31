class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Function to find the root of a set an element belongs to.
        def find_root(element):
            # Path compression: update parent during find operation.
            if parents[element] != element:
                parents[element] = find_root(parents[element])
            return parents[element]
      
        # Function to merge two disjoint sets.
        def union_sets(set1, set2):
            # Find the roots of the sets to which the two elements belong.
            root1, root2 = find_root(set1), find_root(set2)
            if root1 == root2:
                # Elements are already in the same set.
                return
            # Merge the two sets.
            parents[root1] = root2
            # Update the size of the resulting set.
            set_sizes[root2] += set_sizes[root1]

        n = len(grid)
        # Initialization of disjoint set union data structure.
        parents = list(range(n * n))
        set_sizes = [1] * (n * n)
      
        # Build the sets for all 1s in the grid (initial islands).
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value:
                    # Try to union with any neighboring 1s to the left and above.
                    for a, b in [[0, -1], [-1, 0]]:
                        x, y = i + a, j + b
                        if 0 <= x < n and 0 <= y < n and grid[x][y]:
                            # Union the current cell with the neighbor.
                            union_sets(x * n + y, i * n + j)

        # Check for the largest initial island size.
        max_island_size = max(set_sizes)
      
        # Check every 0 in the grid to see if it converts to 1 leading to larger island.
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 0:
                    visited_roots = set()  # Track visited roots to prevent double counting.
                    temp_size = 1  # Start with the current cell being converted to 1.
                    # Check all 4 directions around the current cell.
                    for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        x, y = i + a, j + b
                        if 0 <= x < n and 0 <= y < n and grid[x][y]:
                            root = find_root(x * n + y)
                            # If we haven't already added the size of this island root, add it now.
                            if root not in visited_roots:
                                visited_roots.add(root)
                                temp_size += set_sizes[root]
                    # Update our answer if we found a larger island.
                    max_island_size = max(max_island_size, temp_size)
      
        return max_island_size
