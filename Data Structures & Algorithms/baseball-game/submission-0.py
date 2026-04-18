class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for operation in operations:
            if operation == "D":
                res.append(2 * res[-1])
            elif operation == "+":
                firstRecord = res.pop()
                secondRecord = res[-1]
                res.append(firstRecord)
                res.append(firstRecord + secondRecord)
            elif operation == "C":
                res.pop()
            else:
                res.append(int(operation))

        return sum(res)                             