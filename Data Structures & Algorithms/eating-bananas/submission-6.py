class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r, res = 1, max(piles), max(piles)

        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += -(-p // m)
            if h >= time:
                res = m
                r = m - 1                   
            else:
                l = m + 1

        return res


            
