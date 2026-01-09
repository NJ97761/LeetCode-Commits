class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seen = {}
        freq = {}

        for char in s:
            seen[char] = seen.get(char,0) + 1

        for char in t:
            freq[char] = freq.get(char,0)+ 1
        
        if freq != seen:
            return False
        else:
            return True


        