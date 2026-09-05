class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        used = [False] * len(nums)
        def backtrack():
            if len(nums) == len(permutation):
                res.append(permutation.copy())
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                permutation.append(nums[i])
                used[i] = True
                backtrack()
                permutation.pop()
                used[i] = False
            
        backtrack()
        return res