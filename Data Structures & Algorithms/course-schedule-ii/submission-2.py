class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.done = []
        self.pres = prerequisites
        visiting = set()
        for pre in self.pres:
            if not self.dfs(pre[0], visiting):
                return []
        no_pre = [i for i in range(0, numCourses) if i not in self.done]
        for e in no_pre:
            self.done.append(e)
        return self.done

    def dfs(self, course: int, visiting: set[int]) -> bool:
        if course in visiting:
            return False
        if course in self.done:
            return True
        visiting.add(course)
        for pre in self.pres:
            if course == pre[0]:
                if not self.dfs(pre[1], visiting):
                    return False
        visiting.remove(course)
        self.done.append(course)
        return True
        