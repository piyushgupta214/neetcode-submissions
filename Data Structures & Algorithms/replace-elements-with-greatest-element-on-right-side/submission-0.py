class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        current_max = -1
        j = len(arr) - 1

        while j >= 0:
            new_max = max(current_max, arr[j])
            arr[j] = current_max
            current_max = new_max
            j -= 1

        return arr