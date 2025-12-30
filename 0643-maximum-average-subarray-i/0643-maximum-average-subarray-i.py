class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_state= sum(nums[:k])
        max_sum = window_state

        for i in range(k,len(nums)):
            window_state= window_state - nums[i-k] + nums[i]
            max_sum = max(window_state, max_sum)
        return max_sum/k
        