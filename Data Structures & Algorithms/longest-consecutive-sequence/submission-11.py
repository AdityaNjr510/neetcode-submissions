class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hset = set(nums)
        max_len = 0

        for i in hset:
            if i - 1 not in hset:
                length = 1
                while i + length in hset:
                    length += 1
                max_len = max(length, max_len)
            
        return max_len
