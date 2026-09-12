class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.generateSubsets(0, nums, [], res)
        return res

    def generateSubsets(self,index, nums, curr, res):
            res.append(list(curr))
            for i in range(index, len(nums)):
                curr.append(nums[i])
                self.generateSubsets(i + 1, nums, curr, res)
                curr.pop()