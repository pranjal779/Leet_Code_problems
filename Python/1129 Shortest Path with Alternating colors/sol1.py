class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for start, end in redEdges:
            graph[start].append((end,0))
        
        for start, end in blueEdges:
            graph[start].append((end,1))

        table = [-1 for _ in range(n)]

        for i in [0,1]:
            q = deque()
            seen = set()
            q.append((0, i, 0))

            while(q):
                pos, colour, step = q.popleft()
                if (pos,colour) in seen:
                    continue

                if table[pos] == -1:
                    table[pos] = step
                else:
                    table[pos] = min(table[pos], step)

                seen.add((pos,colour))

                for edge, edgeColour in graph[pos]:
                    if edgeColour != colour:
                        q.append((edge, edgeColour, step+1))
        return table
