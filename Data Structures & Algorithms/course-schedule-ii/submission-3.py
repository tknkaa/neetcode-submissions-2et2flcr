from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)
            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
            
        if len(result) == numCourses:
            return result
        else:
            return []
        