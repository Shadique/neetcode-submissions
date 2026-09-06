class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            #print(stack)
            val = i
            if val[0] in '+-':
                val = val[1:]
            if val.isdigit():
                stack.append(int(i))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if i == '+':
                    stack.append(n1 + n2)
                elif i == '-':
                    stack.append(n1 - n2)
                elif i == '*':
                    stack.append(n1 * n2)
                elif i == '/':
                    stack.append(int(n1 / n2))
            #print(stack)
        return stack[0]