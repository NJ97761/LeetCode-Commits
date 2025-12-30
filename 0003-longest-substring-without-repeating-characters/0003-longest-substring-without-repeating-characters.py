class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window_state = set()
        result = 0

        for right in range(len(s)):
            while s[right] in window_state:
                window_state.remove(s[left])
                left+=1
            window_state.add(s[right])
            result = max(result, right-left+1)
        return result
        