class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify_max(nums)

        currentNum = float('inf')
        while k > 0:
            num = heapq.heappop_max(nums)
            # print(currentNum, num, k)
            # if currentNum != num:
            currentNum = num
            k = k-1
        
        return currentNum

            



        