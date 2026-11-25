class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        negative = x < 0
        x = -x if x > 0 else x
        limit = MIN if negative else MAX

        res = 0
        while x != 0:
            digit = x % -10
            x = (x - digit) // 10

            if res < -214748364:
                return 0

            if res == -214748364 and digit < limit % -10:
                return 0

            res = res * 10 + digit

        return res if negative else -res
        