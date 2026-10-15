class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        a = len(tokens)
        for i in range(a):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
                continue
            b = stack.pop()
            c = stack.pop()
            if tokens[i] == "+":
                stack.append(c + b)
            elif tokens[i] == "-":
                stack.append(c - b)
            elif tokens[i] == "*":
                stack.append(c * b)
            elif tokens[i] == "/":
                stack.append(int(float(c) / b))
        return stack[0]