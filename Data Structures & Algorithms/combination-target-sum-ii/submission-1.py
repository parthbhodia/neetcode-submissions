class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        self.backtrack(0, candidates, [], res, target)
        return res

    def backtrack(self, start, nums, path, res, target):

        if target<0:
            return

        if target==0:    
            res.append(list(path))
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])

            self.backtrack(i+1, nums, path, res, target-nums[i])

            path.pop()