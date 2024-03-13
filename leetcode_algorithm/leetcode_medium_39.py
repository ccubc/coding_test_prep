"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res
    
    
    def dfs(self, candidates, start, target, path, res):
        if target < 0:
            #print("target becomes negative, abandon the stored path")
            return # therefore throwing away the stored path
        if target == 0: # found an answer
            #print(f"found an answer, store path{path} to result")
            res.append(path)
            return
        for i in range(start, len(candidates)):
            #print(f"dfs current path = {path + [candidates[i]]}, candidates={candidates}, new target {target-candidates[i]}, i at {i}")
            self.dfs(candidates, i, target - candidates[i], path + [candidates[i]], res)
            

# 20220301
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start, target, cur_path):
            if target < 0:
                return
            if target == 0:
                res.append(cur_path)
                return
            for i in range(start, len(candidates)):
                dfs(i, target-candidates[i], cur_path + [candidates[i]])
        dfs(0, target, [])
        return res