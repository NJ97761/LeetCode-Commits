class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s
        longest = ""

        for i in range(len(s)):

            odd_palindrome = self.expand_area(s,i,i)

            even_palindrome = self.expand_area(s,i,i+1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        return longest
    def expand_area(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]
        

        