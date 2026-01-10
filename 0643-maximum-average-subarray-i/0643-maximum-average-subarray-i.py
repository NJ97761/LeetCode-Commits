class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        win_state = sum(nums[:k])
        max_avg = win_state/k

        for i in range(k,len(nums)):
            win_state = win_state + nums[i] - nums[i-k]
            avg = win_state/k
            max_avg = max(max_avg, avg)
        return max_avg

            
        