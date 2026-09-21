class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        myStack = []
        operations = {"+", "*", "-", "/"}

        for token in tokens:
            if token in operations:
                val1 = int(myStack.pop())
                val2 = int(myStack.pop())
                if token == "+":
                    myStack.append(val1 + val2)
                elif token == "-":
                    myStack.append(val2 - val1)
                elif token == "*":
                    myStack.append(val1*val2)
                else:
                    myStack.append(val2/val1)
            else:
                myStack.append(token)
        
        return int(myStack[-1])

        