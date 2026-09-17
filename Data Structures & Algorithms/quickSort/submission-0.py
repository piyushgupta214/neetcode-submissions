# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)

    def quickSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:

        if (end-start+1) <=1:
            return pairs 

        pivot = end
        left = start

        for i in range(start,end):
            if pairs[i].key < pairs[pivot].key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1

        temp = pairs[end]
        pairs[end] = pairs[left]
        pairs[left] = temp
    
        # Quick sort left side
        
        self.quickSortHelper(pairs, start, left-1)

        # Quick sort right side
   
        self.quickSortHelper(pairs, left+1, end)

        return pairs

        
        