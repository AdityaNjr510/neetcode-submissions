class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if leftMax > height[l]:
                    water += leftMax - height[l]
                else:
                    leftMax = height[l]
            else:
                r -= 1
                if rightMax > height[r]:
                    water += rightMax - height[r]
                else:
                    rightMax = height[r]

        return water
