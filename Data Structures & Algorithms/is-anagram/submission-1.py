class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create 2 hashmaps and compare their keys and value counts

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        # Count occurrences of each character in s
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        # Count occurrences of each character in t
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        # Compare character frequency dictionaries
        return countS == countT