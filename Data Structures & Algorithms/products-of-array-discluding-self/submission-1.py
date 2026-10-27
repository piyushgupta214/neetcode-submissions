class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #  Brute Force approach - O(n^2)
        # result = []
        # for i in range(len(nums)):
        #     value = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         value *= nums[j]
        #     result.append(value)
        # return result    

        # Prefix and suffix approach 
        # first we calculate from left to right the product of all numbers except the index itself
        #  then we calculate from right to left the product of all numbers except the index itself

        result = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
