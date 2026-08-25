class Solution:
    def calPoints(self, operations: List[str]) -> int:

        operators = {"+", "D", "C"}

        res = []

        for i in range(len(operations)):
            if operations[i] in operators:
                if operations[i] == "+":
                    res.append(res[-1] + res[-2])
                if operations[i] == "D":
                    res.append(res[-1] * 2)
                if operations[i] == "C":
                    res.pop()
            else:
                res.append(int(operations[i]))

        return sum(res)        