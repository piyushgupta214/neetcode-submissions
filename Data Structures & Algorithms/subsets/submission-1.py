class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        outputs = [[]]

        for num in nums:
            new_subset = []

            for sub in outputs:
                new_subset.append(sub + [num])

            outputs.extend(new_subset)

        return outputs