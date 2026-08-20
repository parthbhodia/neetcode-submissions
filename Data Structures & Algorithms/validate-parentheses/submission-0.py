class Solution:
    def isValid(self, s: str) -> bool:
        cmap = {
            '}': '{',
            ')': '(',
            ']':'['
        }

        stack = []
        #iterate the number
        for c in s:
            #check first if the value is in cmap this decides if it is a closing bracket or opening
            if c in cmap:
            # we are checking if the stack is not empty and closing bracket opening value is equal to the last element added
                if stack and cmap[c] == stack[-1]:
                #then pop the last element
                    stack.pop()
                else:

                #it is mandatory for it to have a opening bracket for every closing bracket
                    return False

            else: 
                stack.append(c)

        return True if not stack else False    

                

