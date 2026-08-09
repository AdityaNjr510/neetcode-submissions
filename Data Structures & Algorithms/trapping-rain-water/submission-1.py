class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)

        maxh = height[0]
        leftmax[0] = 0
        for i in range(1, len(height)):
            maxh = max(height[i - 1], maxh)
            leftmax[i] = maxh
        
        maxh = height[len(height) - 1]
        rightmax[len(height) - 1] = 0
        for i in range(len(height) - 2, -1, -1):
            maxh = max(height[i + 1], maxh)
            rightmax[i] = maxh

        water = 0

        for i in range(len(height)):
            curr = min(leftmax[i], rightmax[i]) - height[i]
            if curr > 0:
                water += (curr)

        return water