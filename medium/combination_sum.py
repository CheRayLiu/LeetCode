"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Eg. 
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.recur_num(0,candidates, target,[])
        return self.res
        
    def recur_num(self,index,candidates,target,cur_sol):
        if target == 0:
            self.res.append(cur_sol)
            return
        if index == len(candidates) or target < 0: 
            return
        if target > 0:
            self.recur_num(index,candidates,target-candidates[index],cur_sol+[candidates[index]])
        self.recur_num(index+1,candidates,target,cur_sol) 