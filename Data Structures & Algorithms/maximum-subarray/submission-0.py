class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        L = 0
        currSum = 0
        maxL, MaxR = 0, 0

        for R in range(len(nums)):
            if currSum < 0:
                currSum = 0
                L = R
                maxL = maxR = R

            currSum += nums[R]
            maxSum = max(maxSum, currSum)
            maxR = R

        return maxSum
        