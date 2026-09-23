from collections import deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        res = []

        while q:
            course= q.popleft()
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        if len(res) == numCourses:
            return res
        
        return []
        



        

        
