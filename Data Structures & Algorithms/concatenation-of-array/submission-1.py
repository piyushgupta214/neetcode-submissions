class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0]*len(nums)*2
        k = 0
        n = len(nums) 
        while k < len(nums):
            ans[k] = nums[k] 
            ans[k+n] = nums[k]
            k = k+1
        return ans

        