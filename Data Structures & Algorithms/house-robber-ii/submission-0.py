class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helpler(houses):
            rob1 = 0
            rob2 = 0
            for n in houses:
                newrob = max(rob1,rob2 + n)
                
                rob2 = rob1
                rob1 = newrob
            return rob1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helpler(nums[1:]),helpler(nums[:-1]))