class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r, res = 0, len(nums) - 1, float('inf')
        start, end = nums[0], nums[-1]
        if start < end:
            return start

        while l <= r:
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] >= start:
                l = m + 1
            elif nums[m] <= end:
                r = m - 1

        return res

        