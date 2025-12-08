class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:


            # first Solution
            # for i in nums:
            #     if nums.count(i) > 1:
            #         return True
                
            # return False 


            # Second solution
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False



         # 3rd solution   
        # return True if len(nums) != len(set(nums)) else False
        