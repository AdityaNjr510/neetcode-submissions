class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = defaultdict(int)

        for i in nums:
            hmap[i] += 1

        freq = [[] for i in range(len(nums)+1)]
        for key, v in hmap.items():
            freq[v].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
