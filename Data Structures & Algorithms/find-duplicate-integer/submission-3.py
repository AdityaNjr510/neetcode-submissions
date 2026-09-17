class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0

        while slow != fast or not slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        p1, p2 = 0, slow

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1
        



