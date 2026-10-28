class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        for i in range(len(nums)-2):
            current = nums[i]
            if current > 0:
                break
            if i > 0 and current == nums[i-1]:
                continue
            l = i +1
            r = len(nums)-1
            while l < r:
                threeSum = current + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([current, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result