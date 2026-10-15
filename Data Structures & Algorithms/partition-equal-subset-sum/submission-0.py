class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = {0}

        for n in nums:
            nextDP = dp.copy()

            for t in dp:
                nextDP.add(t + n)

            dp = nextDP

            if target in dp:
                return True

        return False


        