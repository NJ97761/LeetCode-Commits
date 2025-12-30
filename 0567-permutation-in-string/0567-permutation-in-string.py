class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False

        freq={}
        for char in s1:
            freq[char] = freq.get(char,0)+1

        win_state={}
        for char in s2[:len(s1)]:
            win_state[char] = win_state.get(char, 0)+ 1
        
        if win_state == freq:
            return True
        
        for i in range(len(s1),len(s2)):
            left_char = s2[i-len(s1)]
            win_state[left_char] -= 1
            if win_state[left_char] == 0:
                del win_state[left_char]
            
            right_char= s2[i]
            win_state[right_char] = win_state.get(right_char,0)+1
            if win_state == freq:
                return True
        return False

            
        