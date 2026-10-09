class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # convert the list into a max heap 

        # now pop first two items 

        # check the condition if destroyed i.e. x==y pop two new stone if one weight is higher then push it back to heap 
        # and then pop two new stones 

        # keep doing until heap size is > 1

        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 != stone2:
                heapq.heappush_max(stones, stone1-stone2)
        
        if len(stones) > 0: 
            return stones[0]
        else:
            return 0



        