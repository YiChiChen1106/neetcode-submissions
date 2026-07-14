class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        L,R = 0, len(height) - 1
        res = 0
        height_L_MAX = height[0]
        height_R_MAX = height[len(height) - 1]
        while L < R:
            if height_L_MAX < height_R_MAX:
                L += 1
                height_L_MAX = max(height_L_MAX,height[L])
                res += (height_L_MAX - height[L])
            else:
                R -= 1
                height_R_MAX = max(height_R_MAX,height[R])
                res += (height_R_MAX - height[R])
        return res


