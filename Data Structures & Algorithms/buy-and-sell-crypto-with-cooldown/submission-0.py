from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 第 0 天结束时的状态
        hold = -prices[0]      # 第 0 天买入
        sold = float("-inf")  # 第 0 天不可能卖出
        rest = 0              # 第 0 天什么都不做

        for i in range(1, len(prices)):
            price = prices[i]

            # 全部使用昨天的状态，计算今天的状态
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)

            # 统一更新
            hold = new_hold
            sold = new_sold
            rest = new_rest

        return max(sold, rest)