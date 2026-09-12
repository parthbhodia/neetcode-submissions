class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

            nums.sort()
            res = []

            self.backtrack(0, [], nums, target, res)
            return res


    def backtrack(self, index, path, nums, target,res):
        if target == 0 :
            res.append(list(path))
            return

        if target < 0:
            return

        for i in range(index, len(nums)):
                
            path.append(nums[i])
            self.backtrack(i, path, nums, target-nums[i], res )
            path.pop()