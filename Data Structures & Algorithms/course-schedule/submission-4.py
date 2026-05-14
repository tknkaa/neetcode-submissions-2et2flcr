class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.pres = prerequisites
        self.done = set()
        visiting = set()
        for pre in self.pres:
            course = pre[0]
            if not self.dfs(course, visiting):
                return False
        return True

    def dfs(self, course: int, visiting: set[int]) -> bool:
        if course in visiting:
            return False
        if course in self.done:
            return True
        visiting.add(course)
        for pre in self.pres:
            if pre[0] == course:
                if not self.dfs(pre[1], visiting):
                    return False
        self.done.add(course)
        visiting.remove(course)
        return True

