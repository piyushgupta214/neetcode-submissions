class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify_max(nums)

        while k > 1:
            num = heapq.heappop_max(nums)
            k = k-1
        
        return heapq.heappop_max(nums)

            



        