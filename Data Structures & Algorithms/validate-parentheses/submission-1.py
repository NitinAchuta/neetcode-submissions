class Solution:
    def isValid(self, s: str) -> bool:

        myStack = []

        mapping = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in mapping:
                myStack.append(c)
            elif myStack and mapping[myStack[-1]] == c:
                myStack.pop()
            else:
                return False
        
        return len(myStack) == 0


            

            
        
        