class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIdx = {}
        # for i in range(len(nums)):
        #     numIdx[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numIdx:
                return [numIdx[complement], i]
            
            numIdx[nums[i]] = i

        return [-1,-1]