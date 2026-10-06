class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        outputs = [[]]

        for num in nums:
            new_subset = []

            for sub in outputs:
                new_subset.append(sub + [num])

            outputs += new_subset

        return outputs