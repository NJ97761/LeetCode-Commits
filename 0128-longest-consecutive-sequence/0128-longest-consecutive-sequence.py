class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = set(nums)
        max_length = 0

        for num in nums_sorted:
            if (num -1) not in nums_sorted:
                current_num = num
                current_length = 1
            
                while (current_num + 1) in nums_sorted:
                    current_length = current_length + 1
                    current_num = current_num + 1
                max_length =  max(current_length,max_length)
        return max_length



        