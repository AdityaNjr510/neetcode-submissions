class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        maxHeap = stones
        heapq.heapify(stones)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            new_stone = -abs(stone1 - stone2)
            if new_stone < 0:
                heapq.heappush(maxHeap, new_stone)

        if len(maxHeap) == 0:
            return 0
        elif len(maxHeap) == 1:
            return -maxHeap[0]

        