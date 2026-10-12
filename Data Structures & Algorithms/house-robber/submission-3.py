class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # at every index value we can make a choice should we rob it or should we skip it 

        # 2,9,8,3,6

        # for value 2 should i skip or rob it = for rob 
        # for value 9 should i skip or rob it -> 
        # i can either rob 2 or 9 i have to maximize so i would choose 9

        # for value 8 either

        # 2,9,8 = 2+8 = 10  or 9 

        # 10 
        # 2,9,8,3

        # 2,9,10,12, 6
        # 10, 9+3 = 12 
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            temp = dp[1]
            dp[1] = max(dp[1], nums[i]+dp[0])
            dp[0] = temp

        return dp[1]
