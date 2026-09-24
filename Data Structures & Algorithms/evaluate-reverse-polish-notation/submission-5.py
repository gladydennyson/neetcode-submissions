class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])
        operators = ["+", "-", "*", "/"]
        for item in tokens:
            if item in operators:
                item2 = int(stack.pop())
                item1 = int(stack.pop())
                
                result = 0
                if item == '+':
                    result = item1 + item2
                elif item == '-':
                    result = item1 - item2
                elif item == '*':
                    result = item1 * item2
                elif item == '/':
                    result = int(item1 / item2)
                
                stack.append(result) 
            else:
                stack.append(item)
        return stack[0]