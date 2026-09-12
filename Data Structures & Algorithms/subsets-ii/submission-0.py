class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.generateSubsets(0, nums, [], res)
        return res

    def generateSubsets(self,index, nums, curr, res):
            res.append(list(curr))
            for i in range(index, len(nums)):
                if i>index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                self.generateSubsets(i + 1, nums, curr, res)
                curr.pop()