class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # since nums value is 0 <= val <= 100
        # whenever we encountered val, let's set it to -1
        # and then we can sort the array 
        # count = 0

        # for i, num in enumerate(nums):

        #     if num == val:
        #         nums[i] = -1
        #         count += 1


        # nums.sort(reverse=True)
        # return len(nums) - count

        k = 0 

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
