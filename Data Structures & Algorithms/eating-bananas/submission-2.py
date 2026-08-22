class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # init l and r 

        l , r = 1, max(piles)
        #at max you can eat r
        res = r
        #iterate through all the list from start to max a basic step for Binary Search
        while l <= r:
            #get the rate at per hour you can eat this which should not exceed the total hours allocated to us
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            # if it takes us more than h hours to complete then increase the rate of binary search to eat more bananas else reduce it to 
            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1

        return res