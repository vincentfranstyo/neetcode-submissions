class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ')': '(', '}': '{', ']': '['}
        stack = []

        for e in s:
            if e in pairs.values():
                stack.append(e)
            else:
                print(f"e {e}")
                if stack:
                    val = stack.pop()

                    if pairs[e] != val:
                        return False
                else:
                    return False
                
        return len(stack) == 0

