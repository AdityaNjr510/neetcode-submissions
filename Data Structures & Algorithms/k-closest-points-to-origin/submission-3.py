class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        for i in range(len(points)):
            dist = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            points[i] = [-dist, points[i][0], points[i][1]]
        
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)

        res = []
        for p in points:
            res.append([p[1], p[2]])
        return res

