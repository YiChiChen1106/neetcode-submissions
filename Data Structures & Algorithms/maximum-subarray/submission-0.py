class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        for n in nums[1:]:
            curSum = max(n,curSum + n)
            maxSum = max(maxSum,curSum)
        
        return maxSum
        