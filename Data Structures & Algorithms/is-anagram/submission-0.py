class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         
        #if both string is not same then they can't be anagram 
        #store char and their count in map for both string

        #now iterate through one of the map and check in other map if they char exists and its value is equal, if yes then anagram else no
        # 1. If both strings are not the same length, they can't be anagrams
        if len(s) != len(t):
            return False
            
        # 2. Store char and their count in a map for both strings
        map1 = {}
        map2 = {}
        
        for char in s:
            map1[char] = map1.get(char, 0) + 1
            
        for char in t:
            map2[char] = map2.get(char, 0) + 1
            
        # 3. Iterate through one map and check in the other map
        for char in map1:
            if char not in map2 or map1[char] != map2[char]:
                return False # Not an anagram
                
        return True # Yes, it is an anagram


        
            
        