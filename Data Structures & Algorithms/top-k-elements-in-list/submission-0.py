class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # lets store each element in map with recurrence and sort the map based on recurrence 

        # and give the first k elements

        # sorting algo will be nLogn and traversing will ne n so complexity will nlogn

        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) +1

        arr = []

        for num, freq in freqMap.items():
            arr.append([freq, num])
        
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
        
        