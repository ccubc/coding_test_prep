"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

from collections import defaultdict, Counter, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = Counter({i:0 for i in range(numCourses)})
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1
        output = []
        queue = deque([v for v in in_degree if in_degree[v] == 0])
        while queue:
            v = queue.popleft()
            output.append(v)
            for n in adj_list[v]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)
        if len(output) < numCourses:
            return []
        return output


# 20230410
# similar solution but with my own code and understanding

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = collections.defaultdict(int)
        unlock = collections.defaultdict(list)
        # first make a dictionary to record the indegree
        # unlock is the opposite of prerequisites, e.g. pre_requisites: [unlocked courses]
        for p in prerequisites:
            inDegree[p[0]] += 1
            unlock[p[1]].append(p[0])
        # find all the vertex of which their inDegree = 0
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        # expand the graph (BFS)
        res = []
        while queue:
            cur_course = queue.pop(0)
            res.append(cur_course)
            for c in unlock[cur_course]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)
        
        if len(res) == numCourses:
            return res
        return []