class Solution:
    def isValid(self, s: str) -> bool:
        #create a hashmap of valid paranthesis 

        cmap = {
            '}' : '{',
            ']' : '[', 
            ')' : '('    
        }
        stack = []
        for c in s:

            if c in cmap: 
            
                if stack and stack[-1] == cmap[c]:
                    stack.pop()
                else:
                    return False
            else: 

                stack.append(c)

        return True if not stack else False
        

