class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n + 1) * n // 2
        res = total - sum(nums) 
        return res
        