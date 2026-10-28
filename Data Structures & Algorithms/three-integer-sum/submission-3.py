class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            current = nums[i]
            l = i +1
            r = len(nums)-1
            while l < r:
                sum = nums[l] + nums[r]
                if sum + current < 0:
                    l += 1
                elif sum + current > 0:
                    r -= 1
                else:
                    result.add((current, nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(result)