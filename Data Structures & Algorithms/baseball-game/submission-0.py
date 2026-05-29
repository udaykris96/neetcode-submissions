class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out = []
        n = len(operations)
        for i in range(0, n):
            if operations[i] == '+':
                out.append(out[-1] + out[-2])
            elif operations[i] == 'D':
                out.append(out[-1] * 2) 
            elif operations[i] == 'C':
                out.pop()
            else:
                out.append(int(operations[i]))

        return sum(out)
        