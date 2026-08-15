class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in range(len(nums)):
            print(n)
            if nums[n] in hashset: 
                return True
            hashset.add(nums[n])
        return False
                