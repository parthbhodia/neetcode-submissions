class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] 

        for num in nums:
            n = len(res)
            for i in range(n):

                #copy the list at that position 

                temp = list(res[i])

                # add num to that position - this list only has one element will do it for all the elements in the list
                
                temp.append(num)

                # add this subset to the res

                res.append(temp)
        return res

            



        


