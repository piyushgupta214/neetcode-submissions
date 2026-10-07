class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapAnagram = {}

        for str in strs:
            charMap = {}
            for char in str:
                charMap[char] = charMap.get(char,0)+1
            
            # Convert frequency map into a hashable key
            key = tuple(sorted(charMap.items()))

            if key not in mapAnagram:
                mapAnagram[key] = []

            mapAnagram[key].append(str)

        return list(mapAnagram.values())


    
    # iterate through the mapAnagram 
    # find the same count value in mapAnagram and compare it with same count value 
    # and check those are anagram or not, if yes add to result group


        