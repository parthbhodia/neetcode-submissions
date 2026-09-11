class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0, nums, [], res)
        return res

    def backtrack(self, index, nums, path, res):
        #add all the list path not the ref of path to the results
        res.append(list(path))
        #go deep in the tree from the remaining set
        for i in range(index, len(nums)):
            #add the current number to the path list
            path.append(nums[i])
            #everytime we call the backtrack we reduce the range since we are done with the previous numbers, so we do i+1 as a new starting point to go thru among the updated nums/path list
            self.backtrack(i+1, nums, path, res)
            path.pop()