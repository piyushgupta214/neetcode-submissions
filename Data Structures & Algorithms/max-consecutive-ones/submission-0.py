class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # start traversing from index 0
        # and start counting 1, 
        # mark it as max
        # when encountered 0 set counter to 0 and start resetting the counter 
        # update max is counter is greater than max

        max_value = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
                if count > max_value:
                    max_value = count
            else:
                count = 0

        return max_value       
        