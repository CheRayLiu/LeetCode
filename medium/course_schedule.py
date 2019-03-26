"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Time: O(E+V)
Space: O(E*V)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [ [] for _ in range(numCourses)]
        self.visited = [0 for _ in range(numCourses)]
        
        for cur,pre in prerequisites:
            self.graph[cur].append(pre)
        for course in range(numCourses):
            if not self.dfs(course):
                return False
        return True
    def dfs(self, cur):
        if self.visited[cur] == -1:
            return False
        elif self.visited[cur] == 1:
            return True
        self.visited[cur] = -1
        for pre_req in self.graph[cur]:
            if not self.dfs(pre_req):
                return False
        self.visited[cur] = 1
        return True
