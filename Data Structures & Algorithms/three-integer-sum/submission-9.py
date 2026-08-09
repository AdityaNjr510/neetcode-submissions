class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSumSorted(numbers, target):

            l, r = 0, len(numbers) - 1
            res = []

            while l < r:
                if numbers[l] + numbers[r] == target:
                    res.append([numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                elif numbers[l] + numbers[r] < target:
                    l += 1
                else:
                    r -= 1
            return res

        nums.sort()
        res = []

        for i in range(len(nums)):
            comp = twoSumSorted(nums[i+1:], -nums[i])
            if comp:
                for c in comp:
                    r = [nums[i], c[0], c[1]]
                    if r not in res:
                        res.append(r)

        return res

        

