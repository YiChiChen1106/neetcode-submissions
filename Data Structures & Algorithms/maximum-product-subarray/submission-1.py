class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1
        for n in nums:
            temp = curMax * n
            curMax = max(n,n * curMax, n * curMin)
            curMin = min(n, temp, n * curMin)
            res = max(res,curMax)
        return res
        