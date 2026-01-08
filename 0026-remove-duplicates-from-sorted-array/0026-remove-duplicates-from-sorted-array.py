class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # left = 0
        # right = len(nums)-1
        # seen = set()


        # while left < right:
        #     mid = left + (right - left)//2

        #     if nums[mid] == nums[mid + 1] == nums[mid -1]:
        #         seen.append(nums[mid])
        #         right = mid - 1
        #     else:
                
        #         left = mid + 1
        # return seen

        left = 0
        

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                
                left += 1
                nums[left] = nums[right]
                
            
        
        
               
        return left + 1

            
        