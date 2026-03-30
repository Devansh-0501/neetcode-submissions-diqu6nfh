class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                top = stack.pop()
                prevTop = stack.pop()
                stack.append(prevTop + top)

            elif ch == "-":
                top = stack.pop()
                prevTop = stack.pop()
                stack.append(prevTop - top)

            elif ch == "*":
                top = stack.pop()
                prevTop = stack.pop()
                stack.append(prevTop * top)

            elif ch == "/":
                top = stack.pop()
                prevTop = stack.pop()
                stack.append(int(prevTop / top))  # ✅ fixed

            else:
                stack.append(int(ch))  # ✅ push int

        return stack[-1]
