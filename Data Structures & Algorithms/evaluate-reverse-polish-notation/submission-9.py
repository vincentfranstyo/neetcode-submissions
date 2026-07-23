class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                val_a = int(stack.pop())
                val_b = int(stack.pop())
                if token == '+':
                    res = val_b + val_a
                elif token == '-':
                    res = val_b - val_a
                elif token == '*':
                    res = val_b * val_a
                elif token == '/':
                    res = val_b / val_a
                
                stack.append(int(res))
                
                print([_ for _ in stack])
            
        return int(stack.pop())
        
