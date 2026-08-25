class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set ()

        l = 0

        res = 0
        for r in range(len(s)):

            while s[r] in charSet:
                # remove the first one not the whole stack, since it is better to keep addng and comparing the set
                charSet.remove(s[l])

                l += 1

            charSet.add(s[r])
            #this is the real sliding window which we need here
            res = max(res, r - l + 1)

        return res