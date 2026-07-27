class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dayRange = [0 for i in range(len(temperatures))]
        stack = [] # (temp, index)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                dayRange[stackInd] = i - stackInd
            stack.append((temperatures[i], i))
        
        return dayRange