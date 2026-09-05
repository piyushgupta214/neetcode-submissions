class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0]*len(nums)*2
        k = 0
        n = len(nums) #4
        while k < len(nums):
            ans[k] = nums[k] #0,1,2,3
            ans[k+n] = nums[k] #4,5,6,7
            k = k+1
        return ans

        