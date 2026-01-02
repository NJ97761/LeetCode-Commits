class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq={}

        for char in s:
            freq[char] = freq.get(char,0)+1
        for char in t :
            if char not in freq:
                return False
            freq[char] -=1
            if freq[char] < 0:
                return False
        return True
        
        # seen = {}
        # seent = {}
        
        # for i in range(len(s)):
        #     seen[s[i]] = seen.get(s[i],0)+1
        # for j in range(len(t)):
        #     seent[t[j]] = seent.get(t[j],0)+1
        # if seen == seent:
        #     return True
        # else:
        #     return False