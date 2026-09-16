class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # first fill nums1 with nums 2 value and then apply sort ?
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        nums1 = nums1.sort()
        