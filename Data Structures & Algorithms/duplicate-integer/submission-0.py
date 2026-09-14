class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNum = set()
        for num in nums:
             if num not in uniqueNum:
                uniqueNum.add(num)
             else:
                return True

        return False