class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        
        # we can calculate the distance and store the distance and point into in min heap. 

        # and then we can return first k elements from the heap

        maxHeap = []

        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            
            heapq.heappush_max(maxHeap, (distance, point))

            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        res = []
        for val in maxHeap:
            res.append(val[1])
        
        return res

            

            
