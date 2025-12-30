class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        win_state= {}
        max_len= 0

        for right in range(0, len(fruits)):
            win_state[fruits[right]]= win_state.get(fruits[right],0)+1

            while len(win_state) > 2:
                win_state[fruits[left]] -= 1
                if win_state[fruits[left]] == 0:
                    del win_state[fruits[left]]
                left +=1
            max_len=max(max_len, right - left + 1)
        return  max_len
            
        