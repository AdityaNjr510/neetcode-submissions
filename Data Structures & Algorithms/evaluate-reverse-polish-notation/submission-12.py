class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if c == "+":
                    stack.append(num1 + num2)
                if c == "-":
                    stack.append(num1 - num2)
                if c == "*":
                    stack.append(num1 * num2)
                if c == "/":
                    stack.append(int(num1 / num2))
        
        return stack[-1]

        