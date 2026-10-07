class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # let's have a map for a-z characters 

    # first lets take first string and iterate it and add the char count for each char exists in the string

    # now iterate second string and decrease the char count for each char exists in the string 

    # now char map if both are anagram will have 0 count for each char if it is not 0 then both strings are not anagram
        if len(s) != len(t):
            return False

        charMap = {}

        for char in s:
            charMap[char] = charMap.get(char, 0) + 1

        for char in t:
            charMap[char] = charMap.get(char, 0) - 1

        for count in charMap.values():
            if count != 0:
                return False

        return True 
