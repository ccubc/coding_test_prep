"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# 20220412
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use topological sort to check whether there is cycle in graph
        in_degree = collections.Counter({i:0 for i in range(numCourses)})
        adj_list = collections.defaultdict(list)
        for e in prerequisites:
            adj_list[e[0]].append(e[1])
            in_degree[e[1]] += 1
        queue = collections.deque([c for c in in_degree if in_degree[c] == 0])
        output = []
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
        if len(output) < numCourses:
            return False
        return True
            

# 20231007
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegree = {i:0 for i in range(numCourses)}
        unlock = defaultdict(list)
        for p in prerequisites:
            inDegree[p[0]] += 1
            unlock[p[1]].append(p[0])
        queue = []
        ct = 0
        for k, v in inDegree.items():
            if v == 0:
                queue.append(k)
        while queue:
            cur = queue.pop(0)
            ct += 1
            for c in unlock[cur]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)
        if ct == numCourses:
            return True
        return False
                  
            