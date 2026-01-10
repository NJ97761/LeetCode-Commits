class Solution:
    def longestPalindrome(self, s: str) -> int:

        if len(s) == 1:
            return 1
        
        seen = {}

        for char in s:
            seen[char] = seen.get(char,0)+1
        length = 0
        odd_found = False 
        for count in seen.values():
            if count % 2 == 0:
                length += count
            else:
                length += count -1
                odd_found = True
        if odd_found :
            length += 1
        return length

