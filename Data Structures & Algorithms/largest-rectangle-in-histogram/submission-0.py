class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack, maxArea = [], 0

        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
            elif stack[-1][1] < heights[i]:
                stack.append([i, heights[i]])
            else:
                index = 0
                while stack and stack[-1][1] >= heights[i]:
                    index = stack.pop()
                    maxArea = max(index[1] * (i - index[0]), maxArea)
                stack.append([index[0], heights[i]])

        for i in stack:
            maxArea = max(i[1] * (len(heights) - i[0]), maxArea)

        return maxArea


