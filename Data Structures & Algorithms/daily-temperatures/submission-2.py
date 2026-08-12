class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack or t <= stack[-1][1]:
                stack.append([i, t])
            else:
                while stack and t > stack[-1][1]:         
                    popped_index = stack.pop()[0]
                    res[popped_index] = i - popped_index
                stack.append([i, t])

        return res
