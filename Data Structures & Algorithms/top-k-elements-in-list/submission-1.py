
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) +1
        
        heap = []

        for num in freqMap.keys():
            heapq.heappush(heap, (freqMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res