class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):

                if p[j - 1] == "*":
                    # * 匹配 0 次
                    if j >= 2:
                        dp[i][j] = dp[i][j - 2]

                        # * 匹配 1 次或多次
                        if i > 0 and (
                            p[j - 2] == s[i - 1]
                            or p[j - 2] == "."
                        ):
                            dp[i][j] = (
                                dp[i][j] or dp[i - 1][j]
                            )

                elif i > 0 and (
                    p[j - 1] == s[i - 1]
                    or p[j - 1] == "."
                ):
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
        