class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.done = []
        self.pres = prerequisites
        visiting = []
        for pre in self.pres:
            if not self.dfs(pre[0], visiting):
                return []
        no_pre = [i for i in range(0, numCourses) if i not in self.done]
        self.done.extend(no_pre)
        return self.done

    def dfs(self, course: int, visiting: List[int]) -> bool:
        if course in visiting:
            return False
        if course in self.done:
            return True
        visiting.append(course)
        for pre in self.pres:
            if course == pre[0]:
                if not self.dfs(pre[1], visiting):
                    return False
        visiting.remove(course)
        self.done.append(course)
        return True
        