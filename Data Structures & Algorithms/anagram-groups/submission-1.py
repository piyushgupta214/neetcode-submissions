class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapAnagram = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
        
            if key not in mapAnagram:
                mapAnagram[key] = []

            mapAnagram[key].append(word)
            

        return list(mapAnagram.values())



        