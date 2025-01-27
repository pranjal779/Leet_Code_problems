from collections import deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize a 2D array to keep track of prerequisite relationships
        prereq_matrix = [[False] * numCourses for _ in range(numCourses)]
        # Adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        # In-degree count array to keep track of prerequisites count for each course
        indegree = [0] * numCourses
      
        # Populate the graph and in-degree count from the prerequisites list
        for course, next_course in prerequisites:
            graph[course].append(next_course)
            indegree[next_course] += 1
      
        # Initialize a queue with all courses with no prerequisites
        queue = deque([i for i, count in enumerate(indegree) if count == 0])
      
        # Perform a topological sort to determine prerequisite relationships
        while queue:
            current_course = queue.popleft()
            for next_course in graph[current_course]:
                # Mark direct prerequisite relationship as true
                prereq_matrix[current_course][next_course] = True
                # Propagate the prerequisite information
                for course in range(numCourses):
                    prereq_matrix[course][next_course] = prereq_matrix[course][next_course] or prereq_matrix[course][current_course]
                # Reduce in-degree count and add course to queue if it has no remaining prerequisites
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
      
        # Process the queries to check if each query pair has a prerequisite relationship
        return [prereq_matrix[start_course][end_course] for start_course, end_course in queries]
