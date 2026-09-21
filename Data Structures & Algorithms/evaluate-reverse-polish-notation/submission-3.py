class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {"+", "*", "-", "/"}

        myStack = []

        for token in tokens:
            if token in operations:
                val2 = myStack.pop()
                val1 = myStack.pop()
                if token == "+":
                    myStack.append(val1 + val2)
                elif token == "-":
                    myStack.append(val1 - val2)
                elif token == "*":
                    myStack.append(val1*val2)
                elif token == "/":
                    myStack.append(int(val1/val2))
            else:
                myStack.append(int(token))

        return myStack[0]



        
        