class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.visited = set()
        self.edges = edges

        if not self.dfs(0, -1):
            return False

        if len(self.visited) == n:
            return True
        else:
            return False

    def dfs(self, num: int, parent: int) -> bool:
        if num in self.visited:
            return False
        self.visited.add(num)
        for edge in self.edges:
            if (edge[0] == parent and edge[1] == num) or (edge[0] == num and edge[1] == parent):
                continue
            elif edge[0] == num:
                if not self.dfs(edge[1], edge[0]):
                    return False
            elif edge[1] == num:
                if not self.dfs(edge[0], edge[1]):
                    return False
        return True